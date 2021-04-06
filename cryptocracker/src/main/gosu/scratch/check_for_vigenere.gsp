
function slice(text : String, ways : int) : List<String> {
  var slices = new ArrayList<StringBuilder>()
  for(1..ways) {
    slices.add(new StringBuilder())
  }
  for(i in 0..|text.length) slices[i%ways].append(text[i])
  return slices.map(\slice -> slice.toString())
}

for(keylength in 2..6) {
  var slices = slice(TextUtil.despace(Data.withoutwords), keylength)
  var distributions = slices.map(\text -> TextUtil.frequencyCount(text).Values.orderDescending().subList(0, 15))
  
  print(keylength)
  slices.each(\slice -> print(slice))
  for(rank in 0..|10) print(distributions.map(\numbers -> String.format("%.3f", {numbers[rank]})).join("\t"))
  print("")
}
