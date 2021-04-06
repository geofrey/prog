package scratch

class RoundRobinIterator<T> implements Iterator<T> {
  var count : int
  var items : List<T>
  construct(data : List<T>) {
    items = data
    count = -1
  }
  override function hasNext() : boolean { return items.HasElements }
  override function next() : T { count += 1; return items[count % items.Count] }
  override function remove() { items.remove(count % items.Count) }
}