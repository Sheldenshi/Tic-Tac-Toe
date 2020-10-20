import sys
class Game:
	"""Represents a game of Tic-Tac-Toe."""
	def __init__(self, board, player0, player1):
		self.board = board
		self.players = [player0, player1]
		self.turn = 0
		self.winner = None

	def play(self):
		self.board.display()
		while self.winner == None:
			curr_player = self.players[self.turn]
			move = self.ask_for_move()
			#make the move
			self.board.board[move] = curr_player.mark
			self.winner = self.check_winner()
			self.turn = (self.turn + 1) % 2
			self.board.display()
		self.game_over()

	def ask_for_move(self):
		"""
		Returns a move [x, y] from player input.
		Checks if the movie is valid.
		"""
		move = input("\nYou can quit the game by enter exit.\nPlayer" + str(self.turn) + "'s turn: ")
		print("\n")
		if move == "exit":
			quit()
		if len(move) != 1 or not move.isnumeric() or int(move) < 1 or int(move) >9:
			print("Please type in a number between 1-9.\n")
			return self.ask_for_move()
		elif self.board.board[int(move) - 1] != move:
			print("This spot is marked by " + self.board.board[int(move) - 1] + ", please pick an other.\n")
			return self.ask_for_move()
		else:
			return int(move) - 1

	def check_winner(self):
		""" 
		Returns the winner based on current board (0 or 1).
		None is no winner.
		"""
		mark = self.players[self.turn].mark
		board = self.board.board

		for i in range(3):
			#check row:
			if board[i] == board[i + 1] == board[i + 2] == mark:
				return self.turn
			#check col:
			if board[i] == board[i + 3] == board[i + 6] == mark:
				return self.turn
		#check diagonal:
		if board[0] == board[4] == board[8] == mark or board[6] == board[4] == board[2]:
			return self.turn

		return None


	def game_over(self):
		print("Winner is: Player" + str(self.winner) + "\nThis game is over!\n")
		run()

class Board:
	"""Represents one board to a Tic-Tac-Toe game."""
	def __init__(self):
		"""Initializes a new board."""
		self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	def display(self):
		for i in range(0, 9, 3):
			sys.stdout.write(" | ")
			for j in range(3):
				sys.stdout.write(self.board[i + j] + " | ")
			sys.stdout.write("\n")


class Player:
	"""Represents a player."""
	def __init__(self, mark):
		self.mark = mark



def new_game():
	player0 = Player('X')
	player1 = Player('O')
	board = Board()
	return Game(board, player0, player1)

def run():
	init = input("WELCOME TO TIC-TAC-TOE!\nHit ENTER to start a game or type exit to quit.\n")
	if init == "":
		game = new_game()
		game.play()
	elif init == "exit":
		quit()
	else: 
		run()

if __name__ == "__main__":
	run()
