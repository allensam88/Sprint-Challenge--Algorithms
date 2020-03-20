#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the while loop will grow linearly with increasing n

for example if n = 2, then 'a' will be computed only one time, but for n = 3, it will be computed

Also, by evaluating the lines, we can see that the 1st line is a constant
then the line inside the while loop is a constant, which you multiply by the loop

this gives us 1 + 1n, which still levels out to be O(n)

b) O(n^2)

Using the same rationale as above, this evalutates to

1 + (1n * 2n) = 1 + 2n^2 = O(n^2)

c)

for this recursion loop, we need to figure out how many times the function is being called

for n = 

## Exercise II

I think this algorithm should be recursive.
The base condition would be when the eggs stop breaking
it could also work in a binary way.... so maybe it starts off where you drop the egg from the highest floor to see if it breaks.
if it breaks, then go to the middle floor and drop... it it still breaks, then go to the new midpoint and drop again
if it survives the fall, then you are getting closer, so go back up to another new midpoint, and drop again
keep splitting in half until you find the exact floor where it survives and the exact floor where it breaks.

It's like a game of 'hotter, colder' when searching for something blindfolded.

Since this is a form of binary searching, I think Big O could be O(log n).

