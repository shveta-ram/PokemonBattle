# Pokemon Battle
Here’s a Python recreation of a general battle scene from my favorite Pokemon Diamond game. This Python project consists of a focus on the logical aspect of player vs. computer games, hence the minimal UI. I’m currently working on a version that utilizes HTML, CSS, and JavaScript for an appealing visual experience. 

# How does the code work?
With the help of random and the instantiation of player/computer stats, this code relies on user input from the player and an implementation of “smart random” from the computer. 
Player and computer Pokemon types, type weaknesses, moves, and move types are initialized in the code. Move effectiveness ranges are represented with numerical values that are fetched by the random command to make the move effectiveness unpredictable, but also on par with other player statistics so it is not entirely too “random.” (i.e.: Tackle resulting in a critical hit? If you play Pokemon, this makes no sense.) Move effectiveness ranges are a bit different for the player. Since the player has the choice to use any move they please, (regardless of whether it would be effective or not) moves that are not in the opponent’s weakness list will result in a decrease in the move effectiveness range’s upper and lower bounds. The whole code is implemented into a while loop that runs the battle until one player has zero health points. Both sides start with 20 health points. 

# Example
Let’s say we have Turtwig, the grass type Pokemon against Chimchar, the fire type opponent. The moves Chimchar can use will be limited to the types of moves that a Grass type Pokemon will be greatly affected by. If Chimchar’s move set has moves that do not fall under Turtwig’s weakness list, this move will not be used. The computer will now use random to choose between the most effective moves left in Chimchar’s move set. Random will be used again to choose a number in the move effectiveness range to determine how many health points the player will lose when the attack lands. 


