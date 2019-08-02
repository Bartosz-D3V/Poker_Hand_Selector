

# Poker Hand Selector
[![Build Status](https://travis-ci.com/Bartosz-D3V/Poker_Hand_Selector.svg?token=tqZyPRhzSnop7iN2Y7Ug&branch=master)](https://travis-ci.com/Bartosz-D3V/Poker_Hand_Selector)

This application has been written to to quickly select the strongest poker hand among different hands.

# Pre-requisites

Software installed and added to a class path (as a system variable):

 1. Python

In addition, to run the application you will need any console/terminal of your choice, or your favorite Java IDE.

## Executing

To run the application file please navigate to the folder with the source code and run the following command:

    py main.py [args]
Example args:

"T10 TJ TQ TK TA, CJ PJ HJ TK PK"

Cards in first hand (**Straight Flush**):


 1. 10 Tiles
 
 2. Jack Tiles
 
 3. Queen Tiles
 
 4. King Tiles
 
 5. Ace Tiles

 Cards in second hand (**Full House**):
 
 1. Jack Clovers
 
 2. Jack Pikes
 
 3. Jack Hearts
 
 4. King Tiles
 
 5. King Pikes

Outcome of the application should be the first hand as Straight Flush is stronger than Full House.


## Cards Decks
TWO = "2"  

THREE = "3"  

FOUR = "4"  

FIVE = "5"  

SIX = "6"  

SEVEN = "7"  

EIGHT = "8"  

NINE = "9"  

TEN = "10"  

JACK = "J"  

QUEEN = "Q"  

KING = "K"  

ACE = "A"


## Cards Suites
HEARTS = "H"  

TILES = "T"  

CLOVERS = "C"  

PIKES = "P"


## Running tests
In order to run tests, please execute the following command:

    python -m unittest discover tests/

## Lint
In order to run linting, please execute the following command:

    pylama
