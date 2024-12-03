# Advent of Code 2024

This is the code that I've used to find the solutions for this year's Advent of Code puzzles. The ones in this repository will be written in Python, and will likely not be super optimized.

My main goal is to show what I did to get a solution to the problem, while keeping the code easy to follow.

## Running this code and other notes

Since I'm using f-strings (ie. `f"{}"`), these scripts will need to be run in a Python 3 environment. No external libraries should need to be installed, and the only important thing is that the scripts are run from the directory they are in. ie. `python3 day1.py` should be run from the day1 folder.

Day 1 makes use of [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) to more easily create a list of id occurrence counts for calculating the similarity score.

Day 3 makes use of [re](https://docs.python.org/3/library/re.html) to run regular expressions.
