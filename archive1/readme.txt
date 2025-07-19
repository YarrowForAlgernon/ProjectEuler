Description:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Explanation:

In order to find the sum of all multiples we first must find all the multiples of 3 and 5.
We can do this naively by looping over every number between 1 and 1000, and checking if they are either 0 mod 3 or 0 mod 5 (proving divisibility).
This is very slow however, and project euler is all about coming up with the most efficient solutions possible.

When coding, the most efficent code is usually the most understandable, organised and easiest to edit code. This is because in Software dev
the amount of time that can be reduced at runtime by code that is slightly harder to understand and more efficent is negligable compared to
the amount of time taken to read and edit it.

In project euler however, the goal is runtime speed. An indicator of speed can be the number of calculations, based in Big O notation. This roughly
mathematically describes the amount of calculations taken for an algorithim to run in the worst case scenario.
For example, an algorithim that halfs a number repeatedly until it reaches <= 1 can be described as O(log2(n)). This is beacuse this algorithim is logarithmic,
and takes roughly (log2(n)) calculations, where n is the number to half.

E.g, for 10, 10 -> 5 -> 2.5 -> 1.25 -> 0.625. this is 4 calculations, which can roughly be confirmed by log2(10) = 3.32.

And for 200, 200 -> 100 -> 50 -> 25 -> 12.5 -> 6.25 -> 3.125 -> 1.5625 -> 0.78125 or 8 calculations. log2(200) = 7.64.

Hence, the most efficent code is usually an algorithim that has the best big O notation and thus the least amount of calculations.

Thus, project euler is made up of two parts. The mathematical idea behind the code - the algorithim - and the written implementation - the languages,
coding structures and optimisation of code.

Code optimisation is its own topic. Code written in higher level languages can be different, but when compiled can look almost identical due to compiler optimisation and translation. 
This isnt that important since as long as you dont come up with wildly inefficent code, the amount of time gained from purely the implemntation of coding
practices is very small.

The main philosphoy of project euler is to focus less on the actual solution and more on the method that get you there, an empathsis on the understanding
between different fields and thoughts in mathematics and computer science.

Thus, the first 100 solutions on project euler are free to discuss online, but the rest are prohibited. So tjis repository will document my own thoughts
and ideas on the first 100 archives. Solution will be written in both python and java.

