# Greed
This is a game called Greed. 
In this game, rocks ([]) and gems (*) will fall from 
the top of the screen. Your job is to catch the 
falling gems with your basket (#), but avoid the rocks!
Those decrease your score! 
Gameplay continues until you close the game. 
Have fun!

Greed is played according to the following rules:

<li>Gems (*) and rocks (o) randomly appear and fall from the top of the screen.</li>
<li>The player (#) can move left or right along the bottom of the screen.</li>
<li>If the player touches a gem they earn a point.</li>
<li>If the player touches a rock they lose a point.</li>
<li>Gems and rocks are removed when the player touches them.</li>
<li>The game continues until the player closes the window.</li>
  
---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
if you are inside the folder
python ../greed_game
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                        (project root folder)
+-- game                    (source code for game)
    +-- casting               (source code for casting)
        +-- actor           (specific classes)
        +-- artifact        (specific classes)
        +-- cast            (specific classes)
    +-- directing           (source code for directing)
        +-- director        (specific classes)
        +-- score           (specific classes)
    +-- services            (source code for services)
        +-- keybord_service (specific classes)
        +-- video_service   (specific classes)
    +-- shared              (source code for services)
        +-- color           (specific classes)
        +-- point           (specific classes)
+-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
<li> Canyon Atwood</li>
<li> Miguel Prot</li>
<li> Nathan Wall</li>
<li> Rodrigo Loyo</li>