class TicTacToe:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.player = 'X'
        
    def play(self):
        while not self.game_over():
            self.print_board()
            row, col = self.get_move()
            self.board[row][col] = self.player
            self.player = 'O' if self.player == 'X' else 'X'
            
        if self.winner() == 'T':
            print('Tie Game')
        else:
            print(f'{self.winner()} wins!')
            
    def game_over(self):
        if self.winner() != None:
            return True
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True
    
    def winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return row[0]
        
        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        
        return None
    
    def get_move(self):
        while True:
            try:
                row = int(input(f'{self.player} move (row): '))
                col = int(input(f'{self.player} move (col): '))
                if row in [0, 1, 2] and col in [0, 1, 2] and self.board[row][col] == ' ':
                    return (row, col)
                else:
                    print('Invalid move, try again')
            except ValueError:
                print('Invalid input, try again')
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))
            
if __name__ == '__main__':
    game = TicTacToe()
    game.play()
