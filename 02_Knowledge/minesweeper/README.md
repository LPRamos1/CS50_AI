# CS50 Artificial Intelligence - Minesweeper

This project implements an AI agent capable of playing Minesweeper using propositional logic. Unlike a player who simply guesses, this AI builds a knowledge base of sentences and makes logical inferences to identify safe cells and hidden mines with 100% certainty whenever possible.

## 🚀 Key Learning Points

* **Propositional Logic:** Representing the game state as logical sentences where a set of cells equals a specific number of mines.
* **Knowledge Representation:** Using a `Sentence` class to store and update information as the game progresses.
* **Inference by Subset:** Implementing advanced logical deduction: if one sentence is a subset of another, a new, simpler sentence can be inferred by calculating the difference between them.
* **The "Domino Effect":** Automatically updating the entire knowledge base whenever a new mine or safe cell is discovered, which in turn can trigger further discoveries.
* **AI Decision Making:** Distinguishing between "Safe Moves" (logically proven) and "Random Moves" (calculated risks when no certain information is available).

## 📂 Project Structure & Contributions

This project follows a provided distribution code structure, where my primary contribution was the implementation of the logical reasoning engine.

* **`minesweeper.py` (My Implementation):** I developed the complete logic for the `Sentence` and `MinesweeperAI` classes. This includes:
    * Defining how sentences identify certain mines or safe cells.
    * Implementing the `add_knowledge` function to handle new data and recursive inferences.
    * Designing the subset-based deduction system to discover hidden patterns.
* **`runner.py` (Boilerplate):** The graphical user interface and game engine were provided as part of the CS50 AI framework to visualize the AI's performance.

## 🧠 AI Strategy & Logic

1.  **Direct Inference:** If a sentence has a count of `0`, all cells are marked as **Safe**. If the number of cells equals the count, all cells are marked as **Mines**.
2.  **Subset Deduction:** The AI compares all pairs of sentences. If `Sentence A` is a subset of `Sentence B`, it creates a `Sentence C` with the remaining cells and the adjusted mine count.
    * *Example:* `{A, B, C} = 2` minus `{A, B} = 1` results in `{C} = 1`.
3.  **Recursive Update:** Every time a cell is marked as safe or a mine, all existing sentences are updated, potentially simplifying them and revealing new information.

## 🛠️ How to Run

1.  Ensure you have `pygame` installed:
    ```bash
    pip install pygame
    ```
2.  Run the graphical interface:
    ```bash
    python runner.py
    ```
3.  Click **"AI Move"** to let the logic engine take over.