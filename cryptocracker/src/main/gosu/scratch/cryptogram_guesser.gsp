
var cipher = Data.withoutwords//.toLowerCase().replaceAll("[^\\p{Alpha}]", "")

// along the way: counted letter frequencies in the ciphertext and applied ETAOIN SHRDLU

var guesses = {
  '$' -> '$'
  ,'w' -> 'e', 'W' -> 'E'
  ,'y' -> 't', 'Y' -> 'T'
  ,'e' -> 'i', 'E' -> 'I'
  ,'u' -> 'o', 'U' -> 'O'
  ,'l' -> 'a', 'L' -> 'A'
  ,'p' -> 'm', 'P' -> 'M'
  ,'z' -> 's', 'Z' -> 'S'
  ,'o' -> 'h', 'O' -> 'H'
  ,'t' -> 'r', 'T' -> 'R'
  
  ,'u' -> 'w', 'U' -> 'W'
  ,'f' -> 'n', 'F' -> 'N'
}

var wrap_width = 60
print(TextUtil.wrap(cipher, wrap_width))
print(TextUtil.wrap(cipher.toCharArray().toList().map(\ch -> guesses.getOrDefault(ch, ch)).join(""), wrap_width))
