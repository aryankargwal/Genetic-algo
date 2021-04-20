# Genetic-algo

## What is this?
<img src="assets/darwin.jpg"><br>
The program tries to guess the given string using a <b>Generic Algorithm</b>.<br>
Genetic Algorithms much like natural evolution in order to linearly search problems and optimize them.  
A DNA objects holds the strings. They are controled by a population object which manages breeding and the mating pool.

## How does this work?
<img src="assets/genetic.png"><br>
For every generation of strings a score is assigned to compare them which are then converted into probabilities in the skiwscore.<br>
DNA objects have a better chance of getting selected as parents if they have a higher probability.<br>
The breeding function selectes a random pivot and splits the two parents and forms a new dna object.

## How to use it?
Before running the actual file following [Requirements](requirements.txt) have to be installed which can be done by the following:<br>
` pip install -r requirements.txt`<br>
Now running the file:<br>
` python run.py "your argument"`<br>
To further dive deeper into the usage you can use the following command:<br>
`python run.py -h`

## Contribution
The code has been cleaned and restructered by [Aryan](https://github.com/aryankargwal).

## License
Presented repository is under the [MIT License](license.md)
