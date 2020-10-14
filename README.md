# python-game
A puzzle game in Python that I imagined.

Game Instructions

The Board

The game board has three main components:

1)  Tiles - you can move these around to score points.   

2)  Border - outside of the board is a colourful border, these colours correspond to the colours of the tiles. 

3)  Border Generator - this generates a new roof for the board each turn.

Scoring Points:

- Points are scored when a tile enters a coloured gate on the border
- If a tile is immediately next to its corresponding coloured gateway the it automatically enters it
- You score points equivalent to the value of the tile

Moving Tiles:

- You can move tiles around the board as long as there is space
- Tiles can move left or right
- They are affected by gravity
- When a tile moves, its value decreases by 1. You can think off the value as being its ‘movement points’
- Zero tiles are immovable so avoid moving tiles with only 1 movement point.


Ending Your Turn / Lose Condition:

- At the end of your turn the border will rotate 90 degrees clockwise
- Losing - if you have a tile touching the roof of the board when you end your turn you lose.
- New tiles will drop in from the roof at the start of your next turn.

