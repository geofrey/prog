package scratch

class Maperator<T,F> implements Iterator<F> {
  var underlying : Iterator<T>
  var transform : block(item:T):F
  construct(source : Iterator<T>, operation(item:T):F) {
    underlying = source
    transform = operation
  }
  override function hasNext() : boolean { return underlying.hasNext() }
  override function next() : F { return transform(underlying.next()) }
  override function remove() { underlying.remove() }
}