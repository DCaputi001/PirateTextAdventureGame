# PIRATE TEXT ADVENTURE GAME 

## Overview
-This is a simple text-based adventure game where you, a pirate, are on a quest to avenge your fallen crew. To succeed, you must explore various islands, collect important items, and face the fierce Kraken in a final battle. Be wary though—if you're not fully prepared, you may not survive the encounter!

## Objective

Your objective is to explore all the islands, collect six key items, and ultimately defeat the Kraken. Along the way, you will navigate between islands and gather the following items:
-Grenado
-Eyepatch
-Pirate Hat
-Cutlass
-Axe
-Pistol
-To win the game, you need to collect all six items before reaching the Kraken's Lair.

## How to Play
**Move Between Islands:**
Use directional commands to move between the islands. Example commands include:
-go north
-go south
-go east
-go west

**Collect Items:**

When you enter a room with an item, you'll receive a message about its presence. You can collect it by typing:
get itemname
For example, if you see a "Cutlass" nearby, you would type get Cutlass to add it to your inventory.

**Fight the Kraken:**

Once you've collected all six items, venture to "Kraken's Lair" to face the Kraken. If you don't have all the items, the Kraken will defeat you.
If you do have all six items, you will successfully defeat the Kraken and win the game.
Exit the Game:

At any point, you can exit the game by typing exit.

**Rooms**
Here is the layout of the pirate world, with connections between the islands:

-Buccanner Bay (Item: Grenado)
-South: Treasure Cove
-Treasure Cove (Item: No item)
-North: Buccanner Bay
-South: Jolly Roger Isle
-East: Skull Island
-Jolly Roger Isle (Item: Eyepatch)
-North: Treasure Cove
-East: Kraken's Lair
-Kraken's Lair (Boss: Kraken)
-West: Jolly Roger Isle
-Skull Island (Item: Pirate Hat)
-North: Cutlass Cay
-East: Blackbeards Cove
-West: Treasure Cove
-Blackbeards Cove (Item: Pistol)
-West: Skull Island
-Cutlass Cay (Item: Cutlass)
-East: Mermaid Lagoon
-South: Skull Island
-Mermaid Lagoon (Item: Axe)
-West: Cutlass Cay

**Game Features
**
-Inventory System: Track the items you've collected as you explore the islands.
-Navigation: Move between rooms using directional commands (north, south, east, west).
-Item Collection: Find and collect important pirate-themed items to prepare for your final battle.
-Boss Encounter: Face off against the Kraken in the final showdown, but only if you have all six items.

**Game Commands**
-go [direction]: Move to a new location.
-get [itemname]: Collect an item from the current room.
-exit: Exit the game.

**Requirements**
This game is written in Python and has no external dependencies. You just need to have Python installed on your system.

**License**
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.