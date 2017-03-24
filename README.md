# RouletteEngine

A group of indivduals and I were discussing if one could write an algorithm to effectively predict the outcome of a Roulette spin at a rate better than 50%.

I proposed that as each event is independent from each other, there is no algorithm that one could define that would repeatively out do a constant algorithm such as "Pick Black".


## Assumptions
* This simulation proves nothing, as we're relying on pseudo random implementations and such could even be leveraged to produce great results
* The Roulette board has only Red or Black cells (no Green like a real board)


## To Participate
* Create your own class that extends Algorithm.
* Have that class override 

`def guess(self, previous):` 

Where previous is the last guess, and the first guess will have an enum value of Pick.NONE. Return either Pick.RED or Pick.BLACK.


## To Run
Execute app.py like so

`$ python3 app.py [number of runs] [number of rounds per runs]`


## Areas of interest
* https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables
* https://en.wikipedia.org/wiki/Gambler%27s_fallacy