#include <iostream>
#include <vector>
#include "board.h"

// default constructor
Board::Board() {
    board = std::vector<std::vector<int>>(); // Initialize the board
    setBoard(board);
    moveCount = 0;
    setStartPos();
}

// sets the board to all 0's
void Board::setBoard(std::vector<std::vector<int>>& board) {
    for (int i = 0; i < 8; i++) {
        std::vector<int> row;
        for (int j = 0; j < 8; j++) {
            row.push_back(0);
        }
        board.push_back(row);
    }
}

// sets the starting position
void Board::setStartPos() {
    int x, y;

    std::cout << "Enter the x coordinate of the starting position: ";
    std::cin >> x;
    while(x < 1 || x > 8) {
        std::cout << "Invalid x coordinate. Please enter a number between 0 and 7: ";
        std::cin >> x;
    }

    std::cout << "Enter the y coordinate of the starting position: ";
    std::cin >> y;
    while(y < 1 || y > 8) {
        std::cout << "Invalid y coordinate. Please enter a number between 0 and 7: ";
        std::cin >> y;
    }

    move({y-1, x-1});
}

// displays the board and the reference board
void Board::displayBoards() {
    // system("cls"); // Clear the console screen on Windows systems
    // std::cout<<"Main Board:\n";
    // printBoard();
    // std::cout<<"Reference Board:\n";
    // printReferenceBoard();
    // std::cout<<"\npress enter to continue";
    // std::cin.ignore();
}

//prints the board
void Board::printBoard() {
    std::cout<< "  ";

    for (int i = 1; i < 9; i++) {
        std::cout << i << "  ";
    }
    std::cout << std::endl;
    for (int i = 1; i < 9; i++) {
        std::cout << i << " ";
        for (int j = 1; j < 9; j++) {
            if (board[i-1][j-1] < 10) {
                std::cout << " ";
            }
            std::cout<< board[i-1][j-1] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

//prints the reference board
void Board::printReferenceBoard() {
    std::cout<< "  ";

    for (int i = 1; i < 9; i++) {
        std::cout << i << "  ";
    }
    std::cout << std::endl;
    for (int i = 1; i < 9; i++) {
        std::cout << i << " ";
        for (int j = 1; j < 9; j++) {
            if (referenceBoard[i-1][j-1] < 10) {
                std::cout << " ";
            }
            std::cout<< referenceBoard[i-1][j-1] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

//checks if the move is valid
bool Board::checkMove(std::vector<int> move) {
    if (move[0] < 0 || move[0] > 7 || move[1] < 0 || move[1] > 7) {
        return false;
    }
    if (board[move[0]][move[1]] != 0) {
        return false;
    }
    return true;
}

//returns an array of possible moves based on the current position
std::vector<std::vector<int>> Board::possibleMoves(std::vector<int> pos){
    std::vector<std::vector<int>> moves;
    std::vector<int> move;
    move = {pos[0] + 2, pos[1] + 1};

    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] + 2, pos[1] - 1};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] - 2, pos[1] + 1};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] - 2, pos[1] - 1};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] + 1, pos[1] + 2};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] + 1, pos[1] - 2};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] - 1, pos[1] + 2};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    move = {pos[0] - 1, pos[1] - 2};
    if (checkMove(move)) {
        moves.push_back(move);
    }

    return moves;
}

//moves the knight
void Board::move(std::vector<int> pos) {
    if(checkMove(pos) == false) {
        std::cout << "Invalid move." << std::endl;
        return;
    }

    board[pos[0]][pos[1]] = moveCount + 1;
    referenceBoard[pos[0]][pos[1]] = 0;
    currentPos = pos;
    moveCount++;
    updateReferenceBoard();
    displayBoards();
}

//updates the reference board after a move
void Board::updateReferenceBoard() {
    std::vector<std::vector<int>> adjacentPositions = possibleMoves(currentPos);

    for(int i = 0; i < adjacentPositions.size(); i++) {
        referenceBoard[adjacentPositions[i][0]][adjacentPositions[i][1]]--;
    }
}

//returns the value of a move
int Board::checkMoveValue(std::vector<int> move) {
    return referenceBoard[move[0]][move[1]];
}

//solves the board
void Board::solveBoard() {
    while(moveCount < 64) {
        std::vector<std::vector<int>> posMoves = possibleMoves(currentPos);
        
        if (posMoves.size() == 0) {
            std::cout << "No solution found." << std::endl;
            return;
        }

        std::vector<int> lowestPos = posMoves[0];
        int lowestPosMove = checkMoveValue(posMoves[0]);
        for(int i = 0; i < posMoves.size(); i++) {
            int temp = checkMoveValue(posMoves[i]);
            if (lowestPosMove > temp && temp != 0) {
                lowestPos = posMoves[i];
                lowestPosMove = temp;
            }
        }

        move(lowestPos);
    }

    printBoard();
    std::cout << "The board has been solved." << std::endl;
}

//returns the number of moves made
int Board::getMoveCount() {
    return moveCount;
}