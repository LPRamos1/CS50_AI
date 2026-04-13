# 🤖 CS50AI: Introduction to Artificial Intelligence with Python (Harvard University)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CS50AI](https://img.shields.io/badge/CS50AI-Harvard-white?style=for-the-badge&logo=harvard&logoColor=red)
![AI](https://img.shields.io/badge/Focus-Artificial%20Intelligence-blueviolet)

Welcome to my portfolio for **CS50AI**, Harvard University's specialized course on the concepts and algorithms at the foundation of modern artificial intelligence. This repository documents my implementation of AI agents using search, logic, probability, and machine learning.

---

## 📂 Curriculum Structure

The repository is organized by modules, following the official CS50 AI path. Each folder contains the implementation of the core AI logic for the respective projects.

| Module | Core AI Concepts | Key Projects | Status |
| :--- | :--- | :--- | :--- |
| [**00 - Search**](./01_Search) | Pathfinding, BFS, DFS, Minimax, Alpha-Beta Pruning. | [Degrees](./01_Search/degrees), [Tic-Tac-Toe](./01_Search/tictactoe) | ✅ Completed |
| [**01 - Knowledge**](./02_Knowledge) | Propositional Logic, Inferences, Knowledge Bases. | [Knights](./02_Knowledge/knights), [Minesweeper](./02_Knowledge/minesweeper) | ✅ Completed |
| **02 - Uncertainty** | Probability, Bayesian Networks, Markov Models. | PageRank, Heredity | ⏳ In Progress |
| **03 - Optimization** | Constraint Satisfaction, Local Search, Linear Programming. | Crossword | 📅 Upcoming |
| **04 - Learning** | Supervised/Unsupervised Learning, Reinforcement Learning. | Shopping, Nim | 📅 Upcoming |
| **05 - Neural Networks** | Deep Learning, Backpropagation, Computer Vision. | Traffic | 📅 Upcoming |
| **06 - Language** | Natural Language Processing (NLP), Transformers. | Parser, Attention | 📅 Upcoming |

---

## 🏆 Featured Implementations

### [Minesweeper AI](./02_Knowledge/minesweeper)
A logical agent that plays Minesweeper using a **Knowledge Base**. Instead of guessing, the AI represents game data as logical sentences and performs **Inference by Subset** to calculate safe moves with 100% certainty.

### [Tic-Tac-Toe AI](./01_Search/tictactoe)
An unbeatable AI using the **Minimax algorithm**. I optimized the search process by implementing **Alpha-Beta Pruning**, allowing the agent to evaluate game states much faster by skipping irrelevant branches of the decision tree.

### [Degrees](./01_Search/degrees)
A search-based program that finds the shortest path between two actors using **Breadth-First Search (BFS)** on an IMDb-based graph, demonstrating efficient navigation of large datasets.

---

## 🛠️ Tech Stack & Skills

* **Language:** Python 3.12+
* **AI Algorithms:** BFS/DFS, Minimax (Alpha-Beta Pruning), Propositional Logic, Model Checking.
* **Libraries:** `pygame` (visualizers), `logic.py` (logic engine), `copy`, `math`.
* **Dev Tools:** Git/GitHub, VS Code.

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/LPRamos1/CS50_AI.git](https://github.com/LPRamos1/CS50_AI.git)
   cd CS50_AI
