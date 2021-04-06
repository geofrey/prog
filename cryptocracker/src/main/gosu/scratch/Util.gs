package scratch

class Util {
  public static function gcd(x:int, y:int) : int {
    if(x == 0 or y == 0) throw new IllegalArgumentException("non-positive argument")
    
    while(x != y) {
      if(x > y) x -= y
      else y -= x
    }
    return x
  }
  
  public static function memoize<I,O>(generator : block(value:I):O) : block(value:I):O {
    var remembered = new HashMap<I,O>()
    var memoized = \value:I -> {
      if(not remembered.containsKey(value)) remembered.put(value, generator(value))
      return remembered.get(value)
    }
    return memoized
  }
}
