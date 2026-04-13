# CS50 Artificial Intelligence - Tic-Tac-Toe

This project implements an AI agent that plays Tic-Tac-Toe optimally using the Minimax algorithm. The AI is designed to never lose; it will either win or force a draw, regardless of the opponent's moves.

## 🚀 Key Learning Points

* **Minimax Algorithm:** Implementing an adversarial search algorithm used in two-player, zero-sum games.
* **Alpha-Beta Pruning:** Optimizing the Minimax search by skipping branches that cannot influence the final decision, significantly reducing computation time.
* **Recursion:** Using recursive functions (`max_value` and `min_value`) to simulate future game states.
* **Game State Modeling:** Handling board representations, legal moves, and determining terminal states (win/loss/draw).

## 📂 Project Structure & Contributions

This project consists of a logic file and a graphical runner. My work focused on implementing the game engine and the AI decision-making logic.

* **`tictactoe.py` (My Implementation):** I developed all the core functions required for the game, including:
    * `player`, `actions`, and `result` to manage game transitions.
    * `winner` and `terminal` to detect game completion.
    * `minimax` with **Alpha-Beta Pruning** to ensure optimal performance.
* **`runner.py` (Boilerplate):** A Pygame-based interface provided by CS50 to allow human players to play against the AI.

## 🧠 AI Strategy: Minimax with Alpha-Beta Pruning

The AI views the game as a tree of possibilities. **X** is the maximizing player (goal: score of 1), and **O** is the minimizing player (goal: score of -1).

1.  **Optimization:** Without optimization, Tic-Tac-Toe has 255,168 possible game states. By implementing **Alpha-Beta Pruning**, I enabled the AI to "prune" branches of the search tree that are guaranteed to be worse than previously explored moves.
2.  **Unbeatable Logic:** The AI explores every possible outcome of a move to ensure that it always picks the path leading to the best possible result, assuming the opponent also plays optimally.

## 🛠️ How to Run

1.  Ensure you have `pygame` installed:
    ```bash
    pip install pygame
    ```
2.  Run the game:
    ```bash
    python runner.py
    ```
3.  Choose to play as **X** or **O** and try to beat the AI!