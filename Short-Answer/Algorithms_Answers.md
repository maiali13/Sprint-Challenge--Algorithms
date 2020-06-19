
```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

O(n)

Because this loop only executes n times/ grows linearly, aka the number of iterations is equal to n (when n > 1).

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(n log(n))

This algorithm contains two loops whihc we multpily together for the runtime. The outer for loop runs n times. The inner while loop runs log n times.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
O(n)

This is a very simple linear algorithm that calls itself recursively n times.

## Exercise II

### Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

### Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

We can divide the floors in half, (similar to a binary search on a sorted array) and try the middle floor. If the egg breaks, discard the above floors as possiblities, and remember this floor as the highest we need to consider as a possibility for f. We then divide the remaning floors below us in half, moving to that middle floor. If the egg doesn't break, we discard the floors below and only consider the floors above us. Repeating the action of dividing the remaining floors in half until the lowest floor where the egg breaks and assign that to f. Because we are treating this as a binary search, our solution has a runtime complexity of O(log(n)).

i.e.:
with building n = 100
drop the 1st egg at floor 50
    if the egg breaks:
        move to floor 25 and drop 2nd next egg
            if the egg breaks:
                move to floor 13 and drop 3rd egg
                    etc..
            if the egg doesn't break:
                move to floor 37 and drop 3rd egg
                    etc...
    if the egg doesnt break:
        move to floor 75 and drop the 2nd egg
            etc...
