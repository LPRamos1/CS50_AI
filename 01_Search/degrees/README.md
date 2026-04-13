# CS50 Artificial Intelligence - Degrees

This project determines how many "degrees of separation" apart two actors are. Based on the "Six Degrees of Kevin Bacon" game, the AI finds the shortest path between any two actors by identifying the movies they have starred in together.

## 🚀 Key Learning Points

* **Breadth-First Search (BFS):** Implementing BFS to guarantee the shortest path between two nodes in an unweighted graph.
* **State-Space Modeling:** Representing actors as states and movies as actions that transition from one actor to another.
* **Graph Theory:** Navigating large datasets structured as graphs where actors are nodes and shared movie credits are edges.
* **Search Optimization:** Using an explored set and checking for the goal during the frontier expansion to improve algorithm efficiency.

## 📂 Project Structure & Contributions

This project uses a large dataset from IMDb. My implementation focused on the core search algorithm.

* **`degrees.py` (My Implementation):** I implemented the `shortest_path` function. This involved:
    * Setting up the initial state and the frontier using a `QueueFrontier`.
    * Developing the logic to expand nodes and track the connection path through movie/actor pairs.
    * Implementing a backtracking mechanism to reconstruct the path once the target is found.
* **`util.py` (Boilerplate):** Provided the basic data structures for `Node`, `StackFrontier`, and `QueueFrontier`.
* **Data Files:** CSV files containing information about people, movies, and stars.

## 🧠 Search Strategy

To ensure the **shortest** connection is found, I chose **Breadth-First Search (BFS)**.

1.  **Frontier:** A Queue (FIFO) ensures that we check all neighbors at a depth of 1 before moving to depth 2, and so on.
2.  **Explored Set:** Keeps track of visited actors to prevent the algorithm from entering infinite loops or redundant calculations.
3.  **Path Reconstruction:** Once the target actor is found, the AI traverses back through the "parent" pointers of each node to build the final list of movie-actor transitions.

## 🛠️ How to Run

1.  Navigate to the project directory.
2.  Run the program, optionally specifying the dataset folder (large or small):
    ```bash
    python degrees.py large
    ```
3.  Enter the names of two actors when prompted (e.g., *Source: Tom Hanks*, *Target: Kevin Bacon*).
4.  The AI will output the number of degrees of separation and the specific movies that connect them.