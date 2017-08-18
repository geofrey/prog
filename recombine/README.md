(Re)Combine
===

PyGame clone of [Combine](http://www.mindjolt.com/combine.html).

Written in Python 3.x

Requires PyGame version whatever.

Run `recombine.py`.

Play with mouse or keyboard. Drop colored balls. Combine balls to keep them from filling up the board.

* Three or more of a kind, any shape, combine and reduce to a single ball of the next color in the hierarchy.

* The new ball will occupy the leftmost position of the lowest row in the group that was removed.

* When a group combines balls of the highest color (white), no replacement is inserted.

* This is a puzzle game and not an action game, so there's no steering a drop on the way down.

* Making combos will score points, if you care about that. Higher colors are worth more.


Controls
---

**Move the next drop**: Left/Right keys or move the mouse.

**Rotate the drop**: Up arrow or mouse wheel.

**Drop now**: Down arrow or primary mouse button.

