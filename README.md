# SLE-3: Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Project Title:** Graph Search System using BFS and DFS  
**Name:** Priti Ishwar Shinde  
**PRN:** 26UAM304  
**Division:** A

## 1. System Description
The Graph Search System uses BFS and DFS algorithms to find a path from a start node to a goal node. It represents the problem using a graph. BFS uses a queue, while DFS uses a stack. The system displays the path found by each algorithm.

## 2. C4 Model – Context Level
The user provides the start and goal nodes. The Graph Search System processes the graph and displays the search path.

## 3. C4 Model – Container Level
- **Input Module:** Accepts start and goal nodes.
- **Graph Module:** Stores graph connections.
- **Search Engine:** Executes BFS and DFS algorithms.
- **Visited Set:** Tracks visited nodes.
- **Output Module:** Displays the result.

## 4. C4 Model – Component Level
- **Queue / Stack:** Stores nodes waiting to be explored.
- **Visited Set:** Avoids repeated node exploration.
- **Goal Test:** Checks whether the goal is reached.
- **Path Tracker:** Stores the path from start to goal.

## 5. C4 Model – Code Level
- `graph`: Stores graph connections.
- `bfs()`: Searches using Breadth First Search.
- `dfs()`: Searches using Depth First Search.
- `visited`: Stores visited nodes.
- `path`: Stores the path to the goal.

## 6. Design Decisions
The system is divided into simple modules to make it easy to understand and maintain. BFS uses a queue, while DFS uses a stack. A visited set prevents repeated exploration.

## 7. AI Contribution Note
**AI Tool Used:** ChatGPT  
**AI Contribution:** Helped me understand the C4 Model, organize the architecture, and prepare explanations.  
**My Contribution:** I reviewed the design, studied BFS and DFS, and tested the Python code.

## 8. Conclusion
I learned how to represent a software system at four architecture levels. I understood the responsibilities of different modules and the working of BFS and DFS algorithms.
