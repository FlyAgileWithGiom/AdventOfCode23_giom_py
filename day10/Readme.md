wishlist
- turn input into a x,y map
- find S, start path at this position, detect direction
- follow pipe instruction in your direction, update position, register it
  - detect new direction
- note: loop is closed so any detected pipe is a good pipe, no need to look further than the first
[ ] idea: can a regular expression with named groups break it all down? if not, switch/case combination, or mapped array

- [x] follow the connected pipe, register new position in list
- detect again on all directions except one we came from
- keep following and incrementing step until we find the original step we came from
- to get the answer, divide by two, round up