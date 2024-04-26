# Sudoku Solver

## Description
The Sudoku Solver is an interactive console application written in Python designed to solve 9x9 Sudoku puzzles. The program prompts the user to enter each row of the Sudoku grid, checks for validity, and if the board setup is valid, uses a backtracking algorithm to find a solution.

## How It Works

### General Workflow
1. **Start**: The program initiates and welcomes the user.
2. **Input Rows**: Users enter each row of the Sudoku grid.
3. **Validation**: Each row is validated for correct length and content.
4. **Board Setup**: The complete board is displayed and validated for Sudoku rules.
5. **Solving**: The program attempts to solve the Sudoku using backtracking.
6. **Outcome**: The solution is displayed or a message indicating failure.

### Flow Chart
A flowchart is provided as a `Flowchart.png` file in the repository to illustrate the logic flow of the program, detailing each step from initialization to completion.

### Backtracking Algorithm
The solver uses a backtracking algorithm, a depth-first search technique for solving the puzzle:
- **Start Solving**:
  - The process begins by searching for the first empty cell in the Sudoku grid, moving row by row and column by column.

- **Empty Cell Identification**:
  - An empty cell is represented by `0`. The solver scans the grid until it finds such a cell, which then becomes the target for trial placements.

- **Trial Placements**:
  - The algorithm tries to place numbers from `1` to `9` in the identified empty cell. Each number is tested in sequence:
    - The solver checks if placing the current number violates any Sudoku rules:
      - **Row Check**: Ensures the number is not already present in the same row.
      - **Column Check**: Ensures the number is not already present in the same column.
      - **Subgrid Check**: Ensures the number is not already present in the corresponding 3x3 subgrid.

- **Recursive Descent**:
  - If a number is placed successfully without violating any rules, the algorithm calls itself recursively, attempting to solve for the next empty cell using the same process.
  - This step creates a path of choices, where each successful number placement leads deeper into a potential solution.

- **Backtracking**:
  - If at any point the solver determines that no number can be placed in a particular empty cell (all numbers from `1` to `9` have been tried and lead to violations), it backtracks:
    - The algorithm undoes the last successful number placement (the last recursive call where a number was placed without rule violations).
    - It then resumes the number placement trial with the next number in the sequence for the previous cell.

- **Solution or Termination**:
  - This process of placing numbers, recursive descent, and backtracking continues until:
    - **Solution Found**: All cells in the grid are filled correctly, indicating that the puzzle is solved. The algorithm then terminates with a success message.
    - **Exhaustion Without Solution**: All possible number placements have been tried in the initial empty cells without successfully filling the entire grid. The algorithm then terminates, indicating that no solution is possible with the given Sudoku setup.

- **Algorithm Efficiency**:
  - The recursive backtracking method ensures that all potential configurations of numbers on the Sudoku grid are considered. While this method guarantees finding a solution if one exists, it does so by exploring potentially many configurations, making it computationally intensive.


## Testing
To test the Sudoku Solver:
1. **Manual Testing**: Enter known puzzles into the program and verify the output matches expected results.


## Credits


## Usage Instructions
1. Follow the on-screen prompts to enter each row of your Sudoku puzzle.
2. Type `exit` at any input prompt to stop the process.
3. After entering all rows, the program will display the initial board and attempt to solve the puzzle.


