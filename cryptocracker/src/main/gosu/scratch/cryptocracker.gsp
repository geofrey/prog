
function frequencycount(sample : String, length : Integer = null) : Map<Character, Double> {
  if(length == null) length = sample.length
  return sample.toCharArray().toList().partition(\letter -> letter).mapValues(\group -> group.Count as double / length)
}

function compareFrequencies(sample : Map<Character, Double>, reference : Map<Character,Double>) : double {
  var deviation = 0.0
  for(letter in sample.Keys) deviation += Math.abs((sample[letter] - reference.get(letter)) / sample[letter])
  return deviation / sample.Count
}

function differenceFromEnglish(sample : String) : double {
  var sampleFrequency = frequencycount(sample)
  return compareFrequencies(sampleFrequency, Data.englishfrequencies)
}

function ngramCount(text : String, len : int) : Map<String,Integer> {
  var graphs = new HashMap<String, Integer>()
  var i = len
  while(i < text.length) {
    var graph = text.substring(i-len, i)
    if(not graphs.containsKey(graph)) {
      graphs[graph] = 0
    }
    graphs[graph] += 1
    i += 1
  }
  return graphs
}

var a_index : int = 0
function ctoi(letter : char) : int {
  return letter - 'a' - a_index
}
function stoi(letter : String) : int {
  return letter.charAt(0) - 'a' + a_index
}
function itoc(value : int) : char {
  return ((((value - a_index) % 26 + 26) % 26) + 'a') as char
}
function itos(value : int) : String {
  return ((((value - a_index) % 26 + 26) % 26) + 'a') as char as String
}

function applyi(text : String, transform(letter:int):int) : String {
  return text.toCharArray().toList().map(\letter -> itoc(transform(ctoi(letter)))).join("")
}

function applyc(text : String, transform(letter:char):char) : String {
  return text.toCharArray().toList().map(\letter -> transform(letter)).join("")
}

var caesar = \text:String,key:int -> applyi(text, \n -> n+key)
var affine = \a:int,b:int -> \text:String -> applyi(text, \n -> a*n+b)
var power = \text:String,pow:int -> applyi(text, \n -> Math.pow(n,pow) as int)

function vigenere_encode(text : String, key : String) : String {
  var output = new StringBuilder()
  for(letter in text index i) {
    output.append(caesar(letter, ctoi(key.charAt(i%key.length))))
  }
  return output.toString()
}
function vigenere_decode(text : String, key : String) : String {
  var output = new StringBuilder()
  for(letter in text index i) {
    output.append(caesar(letter, -ctoi(key.charAt(i%key.length))))
  }
  return output.toString()
}

function crackCaesar(cipher : String) : Pair<Integer, Double> {
  cipher = cipher.replaceAll(" ", "")
  var encryptKey = 0
  var closest = 999.9
  for(key in 0..25) {
    var test = caesar(cipher, key)
    var difference = differenceFromEnglish(test)
    //print("${crack}: ${difference}%")
    if(difference < closest) {
      closest = difference
      encryptKey = key
    }
  }
  return Pair.make(encryptKey, closest)
}

function caesarSalad(text : String) {
  for(key in 0..25) {
    print(caesar(text, key))
  }
}

function decompose(text : String, ways : int) : List<String> {
  var stripes = (1..ways).map(\n -> new ArrayList<String>())
  for(letter in text index i) {
    stripes[i % ways].add(letter)
  }
  return stripes.map(\stripe -> stripe.join(""))
}

function getLetters(text : String) : Iterator<String> {
  return new Maperator<Integer, String>((0..|text.length).iterator(), \n -> text.substring(n, n+1))
}

function recompose(stripes : List<String>) : String {
  var sources = new RoundRobinIterator<Iterator<String>>(stripes.map(\letters -> getLetters(letters)))
  var output = new StringBuilder()
  for(stripe in sources) {
    if(stripe.hasNext()) {
      output.append(stripe.next())
    } else {
      sources.remove()
      }
  }
  return output.toString()
}

function crackVigenere(cipher : String, minLength : int, maxLength : int) : Pair<String,String> {
  var lowestScore : double = 999.9 // probably higher than any real result
  var bestMatch : String
  var originalKey : String
  
  for(keylength in minLength..maxLength) {
    //print("key length ${keylength} / ${maxlength}") /////
    var key = new ArrayList<String>()
  
    var stripes = new ArrayList<String>()
    for(stripe in decompose(cipher, keylength)) {
      var result = crackCaesar(stripe)
      key.add((result.First + 'a') as Character)
      stripes.add(caesar(stripe, result.First))
      //print(result.Second) /////zgc
    }
    
    var cracked = recompose(stripes)
    
    var keytext = key.join("")
    var encryptKey = affine(-1, 0)(keytext)
    //print("encrypt key: ${encryptKey}") /////
    //print("decrypt key: ${keytext}") ////
    //print("cracked: ${cracked}") /////
    
    var score = differenceFromEnglish(cracked)
    //print("frequency score: ${score}") ////
    if(score < lowestScore) {
      lowestScore = score
      bestMatch = cracked
      originalKey = encryptKey
    }
    //print("best key seen: ${originalkey}") ////
    // print("") ////
  }
  
  return Pair.make(bestMatch, originalKey)
}

function naiveAlign<T>(xs : List<T>, ys : List<T>, score(item:T):Double) : Collection<Pair<T,T>> {
  xs = xs.orderBy(score)
  ys = ys.orderBy(score)
  return (0..xs.Count-1).map(\i -> Pair.make(xs[i], ys[i]))
}

function align<T>(xs : List<T>, ys : List<T>, score(item:T):Double) : Collection<Pair<T,T>> {
  xs = xs.orderBy(score).toTypedArray().toList()
  ys = ys.orderBy(score).toTypedArray().toList()
  var matchLengths = \left:List<T>,right:List<T> -> {
    // normalize
    var shorter = left.Count < right.Count ? left  : right
    var longer =  left.Count < right.Count ? right : left
    while(longer.Count > shorter.Count and longer[longer.Count-1] == null) longer.remove(longer.Count-1) // trim
    while(longer.Count > shorter.Count) shorter.add(shorter.Count, null) // shim
  }
  var deltasquared = \left:List<T>,right:List<T> -> {
    matchLengths(left, right)
    return (0..left.Count-1)
      .map(\i -> Math.pow((right[i] != null ? score(right[i]) : 0) - (left[i] != null ? score(left[i]) : 0), 2))
      .reduce(0.0, \l,r -> l+r)
  }
  
  var currentdeviation = deltasquared(xs, ys)
  
  /**
   * This isn't actually a correct solution. Alignment needs a dynamic-programming approach,
   * and I don't remember what the implementation looks like right now.
   */
  var testAndMaybeUpdate = \xxs:List<T>,yys:List<T> -> {
    var newdeviation = deltasquared(xxs, yys)
    if(newdeviation < currentdeviation) {
      currentdeviation = newdeviation
      xs = xxs
      ys = yys
    }
  }
  
  for(i in 0..xs.Count) {
    var newxs : List<T>
    var newys : List<T>
    
    newxs = xs.copy()
    newxs.add(i, null)
    testAndMaybeUpdate(newxs, ys)
    
    newys = ys.copy()
    newys.add(i, null)
    testAndMaybeUpdate(xs, newys)
  }
  
  return (0..xs.Count-1).map(\i -> Pair.make(xs[i], ys[i]))
}

function crackMonoalphabetic(cipher : String, crib : Map<Character,Character>) : Map<Character,Character> {
  if(crib == null) crib = {}  
  var frequencies = frequencycount(cipher)//.entrySet().mapToKeyAndValue(\e -> e.Value, \e -> e.Key) // reverse map
  var english = Data.englishfrequencies.copy()
  var mapping = new HashMap<Character,Character>()
  mapping.putAll(crib)
  crib.Keys.each(\letter -> frequencies.remove(letter)) // don't try to align these
  crib.Values.each(\letter -> english.remove(letter)) // remove the targets too
  var aligned = align(frequencies.entrySet().toList(), english.entrySet().toList(), \entry -> entry.Value)
  aligned.removeWhere(\entry -> entry.First == null or entry.Second == null)
  
  //mapping.putAll(aligned.mapToKeyAndValue(\e->e.First.Key, \e->e.Second.Key))
  aligned.each(\p -> mapping.put(p.First.Key, p.First.Key))
  
  return mapping
}

function onetime(text : String, pad : String) : String {
  var i = 0
  return applyc(text, \letter:char -> {
    var ch = ((text.charAt(i) - 'a' + pad.charAt(i) - 'a') + 26) % 26 + 'a'
    i+=1
    return ch as char
  })
}

function stream(text : String, iv : String) : String {
  // keystream is key+ciphertext
  var key = new LinkedList<Character>(iv.toCharArray().toList())
  var transform = \letter:char -> {
    var ch = itoc(ctoi(letter) + ctoi(key.remove()))
    key.add(ch)
    
    return ch
  }
  return applyc(text, transform)
}

function counter(i:int) : block():int {
  return \-> {var j = i; i+= 1; return j}
}

function twist(torsion : int, offset : int) : block(text:String):String {
  return \text:String -> {
    var clock = counter(0)
    return applyi(text, \letter -> letter + clock()*torsion + offset)
  }
}
//print(twist(1,-1)("aaaaaaa"))

var spacetext = Data.cryptogram1

var ciphertext = TextUtil.despace(spacetext)

function show(text:String) {
  text = TextUtil.repunctuate(text, spacetext)
  //text = TextUtil.wrap(text, 2*80)
  print(text)
}

print(spacetext)

// CIPHER TYPES

// affine
/*
print("brute-force every affine pair")
for(slope in 1..26) {
  if(Util.gcd(slope, 26) > 1) continue
  print(slope)
  for(offset in 0..25) {
    show(affine(slope, offset)(ciphertext))
  }
  print("")
}
*/


// Vigenere
/*
print("crack vigenere")
var deVig = crackVigenere(ciphertext, 2, 15)
show(deVig.First)
print(deVig.Second)
print("(hand-tune key)")
show(vigenere_decode(ciphertext, "callidus")) // <-- found solution for 'withoutwords'
*/

/*
// frequency and digraphs and trigraphs, oh my
print("ngrams")
for(length in 1..3) {
  var frequencies = ngramCount(ciphertext, length)
  for(point in frequencies.entrySet().orderByDescending(\entry -> entry.Value)) {
    print("${point.Key}: ${point.Value}")
  }
}
*/

/*
// not l^n
print("powers, or something")
var powertext = ciphertext
for(foo in 1..10) {
  print(power(powertext, foo))
}
*/

/*
// self-encrypt each letter?
print("squares")
for(n in 0..25) {
  var stretch = affine(2,n)(ciphertext)
  //print(wrap(respace(stretch, spacewords), 80))
  print(respace(stretch, spacewords))
  //print(differenceFromEnglish(stretch))
  //print("")
}
*/

// Monoalphabetic

var guesses : Map<Character, Character> = {
}
var translation = crackMonoalphabetic(ciphertext, guesses)
print(translation.entrySet().map(\e -> "${e.Key} ${e.Value}").join("\n"))
print(Data.englishfrequencies.Keys.subtract(translation.Keys).join(" "))
var translated = applyi(ciphertext, \letter -> translation.getOrDefault((letter + 'a') as char, 'x') - 'a')
show(translated)
print("")


/*
// stream cipher  
print("stream")
for(key in 'a'..'z') {
  show(stream(ciphertext, key as char as String))
  print("")
}
*/


/*
print("affine-ish")
var solved = twist(1, 0)(stream(ciphertext, "a")) // found solution for 'TCASmessage'
show(solved)
*/
