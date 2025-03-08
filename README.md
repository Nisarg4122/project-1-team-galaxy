1.Define the Game Concept
    
    Game Genre: Spaceship battle and space exploration.
    Core Gameplay: Players explore the galaxy, engage in battles, and manage inventory.
    Player Interaction: Players can choose to explore, fight, or manage their inventory.

2. Create the Main Menu

   Options:
      - New Game: Start a new game.
      - Load Game: Load a saved game.
      - Exit: Exit the game.

    Implementation:
      - Design a user interface (UI) for the main menu.
      - Program the functionality for each option (e.g., starting a new game, loading saved data, or exiting).

3. Player Setup
   Player Details:
       - Name: Allow the player to input their name.
       - Character Type: Let the player choose a character type (e.g., pilot, engineer, etc.).
   Implementation:
       - Create a UI for player input.
       - Store player details for use throughout the game.

4. Game Loop

Game Options:

  - Explore Galaxy: Show planets and space stations, and display facts about each.
  - Enter Battle: Allow the player to choose weapons, armor, and engage in combat.
  - Check Inventory: List items and their stats.
  - Save Game: Save the current game state.
  - Exit: Exit the game.

Implementation:

- Create a loop that continuously presents these options to the player.
- Program the logic for each option:
      * Explore Galaxy: Generate a list of planets/space stations with descriptions.
      * Enter Battle: Implement a combat system where players can choose weapons and armor.
      * Check Inventory: Display the player’s inventory with item stats.
      * Save Game: Save the player’s progress (e.g., inventory, stats, location).
      * Exit: Allow the player to exit the game.

5. Check Inventory

Inventory Management:
Display a list of items the player has collected.
Show stats for each item (e.g., weapon damage, armor defense).

6. Update Player Stats

Stats to Track:
    - Health: Player’s current health.
    - XP: Experience points earned from battles or exploration.

7. Save and Exit
   - Save Game: Save the player’s current state (e.g., inventory, stats, location).
   - Exit Game: Allow the player to exit the game and return to the main menu.
  
