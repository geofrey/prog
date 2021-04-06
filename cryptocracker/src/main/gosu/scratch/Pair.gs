package scratch

class Pair<F,S> {
  var f : F as First
  var s : S as Second
  construct(irst : F, econd : S) {
    f = irst
    s = econd // lol
  }
  public static function make<P,Q>(irst : P, econd : Q) : Pair<P,Q> {
    return new Pair<P,Q>(irst, econd)
  }
}