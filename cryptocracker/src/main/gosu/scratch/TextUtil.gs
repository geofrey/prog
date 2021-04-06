package scratch

class TextUtil {
  
  public static function wrap(text : String, width : int) : String {
    var buffer = new StringBuilder(text)
    var i = width
    while(i < buffer.length()) {
      while(buffer.substring(i, i+1).Alphanumeric) {
        i -= 1
      }
      buffer.replace(i, i+1, "\n")
      i += width
    }
    return buffer.toString()
  }
  
  private static function test_wrap() {
    print(wrap("", 10))
    print(wrap("beep boop", 0))
    print(wrap("easy", 50))
    print(wrap("short short short short short short short short short", 10))
    print(wrap("medium medium medium medium medium medium medium medium", 20))
    print(wrap("long long long long long long long long long long long long long long long long long long", 80))
    print(wrap("mmmmoooonnnnoooolllliiiitttthhhhiiiicccc", 10))
  }
  
  public static function frequencyCount(text : String) : Map<Character, Float> {
    return text.replaceAll("[^\\p{Alpha}]", "").toCharArray().toList().partition(\ch -> ch).mapValues(\list -> list.Count as float / text.length)
  }
  
  public static function despace(text : String) : String {
    //return text.replaceAll("\\p{Alpha}", "") // wtf
    return text.replaceAll("[^\\p{Alpha}]", "").toLowerCase()
  }

  public static function repunctuate(letters : String, original : String) : String {
    var letterSource = letters.toCharArray().toList().iterator()
    var buffer = new StringBuilder()
    for(character in original.toCharArray()) {
      if(Character.isLetter(character) and Character.isUpperCase(character)) buffer.append(Character.toUpperCase(letterSource.next()))
      else if(Character.isLetter(character) and Character.isLowerCase(character)) buffer.append(Character.toLowerCase(letterSource.next()))
      else buffer.append(character)
    }
    return buffer.toString()
  }
}
