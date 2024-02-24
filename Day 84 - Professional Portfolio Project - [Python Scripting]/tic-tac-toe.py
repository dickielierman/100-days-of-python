class TicTacToe:
    def __init__(self):
        self.this_game = {'row_1': [' ', ' ', ' '],
                          'row_2': [' ', ' ', ' '],
                          'row_3': [' ', ' ', ' ']}
        self.player = 'X'

    def check_open(self, col, row):
        if self.this_game[f'row_{row}'][col - 1] == ' ':
            return True
        else:
            return False

    def set_for_player(self, col, row):
        self.this_game[f'row_{row}'][col - 1] = self.player

    def is_win(self):
        winner = False
        # check rows for win
        for row in ['1', '2', '3']:
            if not winner:
                row_list = self.this_game[f'row_{row}']
                winner = self.all_equal_not_empty(row_list)
        for col in [1, 2, 3]:
            if not winner:
                first_values = [self.this_game[f'row_{row}'][col - 1] for row in ['1', '2', '3']]
                winner = self.all_equal_not_empty(first_values)
        if not winner:
            diagonal_values = [self.this_game['row_1'][0], self.this_game['row_2'][1], self.this_game['row_3'][2]]
            winner = self.all_equal_not_empty(diagonal_values)
        if not winner:
            diagonal_values = [self.this_game['row_1'][2], self.this_game['row_2'][1], self.this_game['row_3'][0]]
            winner = self.all_equal_not_empty(diagonal_values)
        return winner

    def all_equal_not_empty(self, lst):
        # Check if all elements are equal to the first element and not equal to the specified value
        return all(item == lst[0] and item != ' ' for item in lst)

    def game_board(self):
        print('   c1  c2  c3')
        print(f'r1 {self.this_game["row_1"][0]} | {self.this_game["row_1"][1]} | {self.this_game["row_1"][2]}')
        print('   ---------')
        print(f'r2 {self.this_game["row_2"][0]} | {self.this_game["row_2"][1]} | {self.this_game["row_2"][2]}')
        print('   ---------')
        print(f'r3 {self.this_game["row_3"][0]} | {self.this_game["row_3"][1]} | {self.this_game["row_3"][2]}')
        print()

    def play_game(self):
        while True:
            self.game_board()
            # Choose column
            column_choice = input(f'Player "{self.player}" Enter a column number 1, 2, or 3: ')
            while column_choice not in ['1', '2', '3']:
                column_choice = input(f'Player "{self.player}" Enter a column number 1, 2, or 3: ')
            # Choose row
            row_choice = input(f'Player "{self.player}" Enter a row number 1, 2, or 3: ')
            while row_choice not in ['1', '2', '3']:
                row_choice = input(f'Player "{self.player}" Enter a row number 1, 2, or 3: ')
            player_col = int(column_choice)
            player_row = int(row_choice)
            space_available = self.check_open(player_col, player_row)
            if space_available:
                self.set_for_player(player_col, player_row)
                if self.is_win():
                    print(f'Player {self.player} wins!')
                    self.game_board()
                    play_again = input('Would you like to play again? y or n: ').lower()
                    while play_again not in ['y', 'n']:
                        play_again = input('Would you like to play again? y or n: ').lower()
                    if play_again == 'n':
                        print('Thanks for playing, see you again soon...')
                        break
                    else:
                        self.this_game = {'row_1': [' ', ' ', ' '],
                                          'row_2': [' ', ' ', ' '],
                                          'row_3': [' ', ' ', ' ']}
                        self.player = 'X'
                else:
                    self.player = 'O' if self.player == 'X' else 'X'
            else:
                print()
                print('Sorry, that space is already taken.')


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()