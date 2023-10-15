class TicTacToe:

    def __init__(self):
        self._board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # each position can be 0, 1, 2
        self._player_turn = 1 # start with player 1, toggle with 2
        self._result = None

    def _toggle_player_turn(self):
        self._player_turn = 2 if self._player_turn == 1 else 1

    def _print_board(self):
        for row in self._board:
            print(row)

    @staticmethod
    def _check_direction_result(direction):
        player_first_found = None
        for spot in direction:
            if spot == 0:
                return False

            if player_first_found is None:
                player_first_found = spot
            elif spot != player_first_found:
                return False

        return True

    def _check_game_result(self):
        # result can be None -> keep playing, 0 -> tie, 1 or 2
        # Check horizontal
        for row in self._board:
            direction = row
            result = self._check_direction_result(direction)
            if result:
                return True

        for col in s

        return False


    def make_move(self, position_x, position_y):
        if self._result is None:
            print('Sorry game is over.')
            return None

        # First check that position is valid, within board range and not occupied
        if position_x > 2 or position_y > 2:
            print('Invalid move. Outside of board range. Try again.')
            return None

        if self._board[position_x][position_y] != 0:
            print('Position already occupied. Try again')
            return None

        self._board[position_x][position_y] = self._player_turn
        self._print_board()
        result = self._check_game_result()
        if result:
            print(f'Player {result} wins.')
        elif result == 0:
            print('Tie!')
        else:
            self._toggle_player_turn()

game = TicTacToe()
game.make_move(0, 1)
