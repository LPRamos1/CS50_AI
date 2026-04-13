# CS50 Artificial Intelligence - Knights

This project solves classic "Knights and Knaves" puzzles using Propositional Logic. In these puzzles, each character is either a Knight (who always tells the truth) or a Knave (who always lies). The goal is to determine the identity of each character based on a set of sentences they speak.

## 🚀 Key Learning Points

* **Propositional Logic:** Representing complex statements using logical connectives such as `And`, `Or`, `Not`, `Implication`, and `Biconditional`.
* **Biconditional Operators:** Using `Biconditional` to represent the core rule of the puzzle: a statement is true if and only if the person speaking it is a Knight.
* **Model Checking:** Utilizing a model-checking algorithm to iterate through all possible worlds (combinations of true/false for each symbol) to find which identity is consistent with the knowledge base.
* **Knowledge Engineering:** Translating human language (e.g., "We are the same kind") into formal logical structures.

## 📂 Project Structure & Contributions

This project follows a distribution code structure focused on the `logic.py` engine. My work was concentrated on the knowledge engineering aspect.

* **`puzzle.py` (My Implementation):** I implemented the logical sentences for Puzzles 0 through 3. This involved defining the initial constraints for each character (they must be either a Knight or a Knave, but not both) and translating their spoken statements into logical formulas.
* **`logic.py` (Boilerplate):** This file contains the classes for logical connectives and the `model_check` function used to solve the puzzles.
* **`main` Function (Boilerplate):** Handles the output and execution of the model-checking logic.

## 🧠 Logical Strategy

The foundation of each puzzle is the **General Rule**:
> `Character is a Knight ↔ Statement spoken by Character is True`

### Implementation Example (Puzzle 2)
In Puzzle 2, A says "We are the same kind" and B says "We are of different kinds."
* **A's Logic:** `Biconditional(AKnight, Biconditional(AKnight, BKnight))`
* **B's Logic:** `Biconditional(BKnight, Not(Biconditional(BKnight, AKnight)))`

By combining these biconditionals with the rule that one cannot be both a Knight and a Knave, the AI evaluates every possibility and identifies the only valid solution.

## 🛠️ How to Run

1.  Navigate to the project directory.
2.  Run the solver using Python:
    ```bash
    python puzzle.py
    ```
3.  The program will output the solution (Knight or Knave) for each character in Puzzles 0, 1, 2, and 3.