🐍 Snake Game (Python)

A classic Snake Game built using Python. The project includes basic game mechanics along with a simple AI mode that automatically moves the snake toward food while avoiding obstacles.

📁 Project Structure
snake-game/
│
├── main.py        # Entry point of the game
├── snake.py       # Snake class and movement logic
├── level.py       # Game level and obstacle management
├── settings.py    # Game configuration (speed, size, etc.)
├── ai.py          # AI logic for automatic snake movement
└── README.md      # Project documentation
🎮 Features

Classic Snake gameplay

Score tracking

Collision detection (walls, obstacles, self)

Configurable settings

Simple AI mode that:

Moves toward food

Avoids collisions with body and obstacles

🧠 AI Logic

The AI evaluates possible moves and prioritizes directions that reduce the distance to the food while avoiding unsafe positions.

If no safe move toward the food is available, it selects a random direction.

🛠 Requirements

Python 3.x

(If using Pygame)

pip install pygame
▶️ How to Run

Clone the repository:

git clone https://github.com/noormaahnaveed2/snake-game.git

Navigate into the project directory:

cd snake-game

Run the game:

python main.py
🎯 Controls

(Modify if different in your implementation)

Arrow Keys – Move snake

ESC – Quit game

📌 Customization

You can modify game behavior in:

settings.py → Change speed, grid size, window size

level.py → Add or adjust obstacles

ai.py → Improve AI logic

🚀 Future Improvements

Smarter pathfinding AI (A* algorithm)

Multiple difficulty levels

Sound effects

High score saving

Multiplayer mode

📄 License

This project is for educational purposes. Feel free to modify and expand it.
