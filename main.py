from Vhello import Vhello
from AI import Random_AI  # Import the AI strategies you want to demonstrate
from Player import Human, Computer

def main():
    game = Vhello()
    # You can set up the initial game state if needed
    # game.setup_initial_state()

    player1 = Human(game, Vhello.B)
    player2 = Computer(game, Vhello.W, Random_AI(game, Vhello.W))

    while not game.game_finished():
        print_board(game.board)  # Print the game board
        if game.turn == player1.player:
            player1.play()
        else:
            player2.play()

    print_board(game.board)  # Print the final game board
    if game.scoreB > game.scoreW:
        print("Player B (Black) wins!")
    elif game.scoreW > game.scoreB:
        print("Player W (White) wins!")
    else:
        print("It's a tie!")

def print_board(board):
    # Print the game board in a simple format
    for row in board:
        print(" ".join(row))
    print()

if __name__ == "__main__":
    main()