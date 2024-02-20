import random

class RockPaperScissors:
    CHOICES = ['rock', 'paper', 'scissors']
    QUIT = 'quit'
    WINNING_COMBOS = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    RESULTS = {
        'tie': "It's a tie!",
        'user': "You win!",
        'computer': "Computer wins!"
    }

    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.CHOICES)

    def get_user_choice(self):
        prompt = f"Enter {', '.join(self.CHOICES)} (or '{self.QUIT}' to stop): "
        choice = input(prompt).lower()
        while choice not in self.CHOICES + [self.QUIT]:
            choice = input("Invalid choice. " + prompt).lower()
        return choice

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif self.WINNING_COMBOS[user_choice] == computer_choice:
            return 'user'
        else:
            return 'computer'

    def play_round(self):
        user_choice = self.get_user_choice()
        if user_choice == self.QUIT:
            return False
        computer_choice = self.get_computer_choice()
        print(f"Computer chose {computer_choice}.")
        winner = self.determine_winner(user_choice, computer_choice)
        print(self.RESULTS[winner])
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
        print(f"Score - You: {self.user_score}, Computer: {self.computer_score}\n")
        return True

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")
        try:
            while self.play_round():
                pass
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Final scores:")
        finally:
            print(f"Final Score - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
