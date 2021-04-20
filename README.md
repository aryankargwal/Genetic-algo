# Genetic-algo

## What is this?

The program tries to guess the given string using a generic algorithm.  
Genetic Algorithms much like natural evolution in order to linearly search problems and optimize them.  
A DNA objects holds the strings. They are controled by a population object which manages breeding and the mating pool.

## How does this work?
For every generation of strings a score is assigned to compare them which are then converted into probabilities in the skiwscore
DNA objects have a better chance of getting selected as parents if they have a higher probability.
The breeding function selectes a random pivot and splits the two parents and forms a new dna object.

## What can I control?

* end = "Github" -> The target string
* pop = 200 -> Population of each generation
* mutrate = 0.1 -> Probability of mutation

With the following variables the output

```
Gwqwuk 4 2
Gwqwub 9 3
Gwqwub 12 4
Giqwub 20 5
GiZhua 24 6
GiZhub 35 7
GiZhub 40 8
GiZhub 45 9
Gitwub 50 10
Github 66 11
0.09699082374572754 sec
```

Output text format:-



  "Best string of generation"  -  Score  -   Generation Number 
