#ifndef BOARD_H
#define BOARD_H

#include <iostream>
#include <vector>

class Board {
    public:
        std::vector<int> currentPos; // the current position of the knight
        
        Board(); // default constructor
        std::vector<std::vector<int>> possibleMoves(std::vector<int> pos); // returns an array of possible moves based on the current position
        void printBoard(); // prints the board
        void setStartPos(); // sets the starting position
        void move(std::vector<int> pos); // moves the knight
        bool checkMove(std::vector<int> move); // checks if the move is valid
        void solveBoard(); // solves the board
        int getMoveCount(); // returns the number of moves made
        int checkMoveValue(std::vector<int> move); // returns the value of a move
        void updateReferenceBoard(); // updates the reference board
        void printReferenceBoard(); // prints the reference board
        void displayBoards(); // displays the board and the reference board

    private:
        std::vector<std::vector<int>> board; // the board
        void setBoard(std::vector<std::vector<int>>& board); // sets the board to all 0's
        int moveCount; // the number of moves made
        std::vector<std::vector<int>> referenceBoard = {
            {2,3,4,4,4,4,3,2},
            {3,4,6,6,6,6,4,3},
            {4,6,8,8,8,8,4,3},
            {4,6,8,8,8,8,6,4},
            {4,6,8,8,8,8,6,4},
            {4,6,8,8,8,8,4,3},
            {3,4,6,6,6,6,4,3},
            {2,3,4,4,4,4,3,2}
        }; // the reference board
};

#endif
