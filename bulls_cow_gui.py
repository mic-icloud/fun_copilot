import random
import tkinter as tk

def random_string(length):
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:length])

def guess_result(guess, secret_code):
    bulls = sum(1 for g, s in zip(guess, secret_code) if g == s)
    cows = sum(1 for g in guess if g in secret_code) - bulls
    return cows, bulls

class Game:
    def __init__(self, length):
        self.secret_code = random_string(length)
        self.guesses_remaining = 10
        self.window = tk.Tk()
        self.window.title("Cows and Bulls")
        self.window.geometry("400x300")
        self.instructions_label = tk.Label(
            self.window, text="Enter a guess with no repeated digits:"
        )
        self.instructions_label.pack()
        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.pack()
        self.submit_button = tk.Button(
            self.window, text="Submit", command=self.submit_guess
        )
        self.submit_button.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
        self.guesses_remaining_label = tk.Label(
            self.window,
            text=f"Guesses remaining: {self.guesses_remaining}",
        )
        self.guesses_remaining_label.pack()
        self.length_label = tk.Label(
            self.window, text=f"Secret code length: {length}"
        )
        self.length_label.pack()

    def run(self):
        self.window.mainloop()

    def submit_guess(self):
        guess = self.guess_entry.get()
        if (
            len(guess) != len(self.secret_code)
            or not guess.isdigit()
            or len(set(guess)) != len(guess)
        ):
            self.result_label.config(text="Invalid guess")
        else:
            cows, bulls = guess_result(guess, self.secret_code)
            self.result_label.config(
                text=f"Misplaced: {cows}, Correct: {bulls}"
            )
            self.guesses_remaining -= 1
            self.guesses_remaining_label.config(
                text=f"Guesses remaining: {self.guesses_remaining}"
            )
            if bulls == len(self.secret_code):
                self.result_label.config(text="You win!")
                self.submit_button.config(state="disabled")
            elif self.guesses_remaining == 0:
                self.result_label.config(
                    text=f"You lose! The secret code was {self.secret_code}"
                )
                self.submit_button.config(state="disabled")

if __name__ == "__main__":
    game = Game(4)
    game.run()