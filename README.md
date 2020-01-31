# Genetic-algo

The program tries to guess the given string using a generic algorithm
A DNA objects holds the strings. They are controled by a population object which manages breeding and the mating pool.

For every generation of strings a score is assigned to compare them which are then converted into probabilities in the skiwscore
DNA objects have a better chance of getting selected as parents if they have a higher probability.

The breeding function selectes a random pivot and splits the two parents and forms a new dna object. 
