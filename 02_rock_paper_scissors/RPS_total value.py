from enum import Enum

class SignName(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

DECODER_RULES = {
    SignName.ROCK: ["A", "X"],
    SignName.PAPER: ["B", "Y"],
    SignName.SCISSOR: ["C", "Z"]
}

GAME_RULES = {
    SignName.ROCK: SignName.SCISSOR,
    SignName.SCISSOR: SignName.PAPER,
    SignName.PAPER: SignName.ROCK
}

class Sign:
    def __init__(self, code) -> None:
        for name, rule in DECODER_RULES.items():
            if code in rule:
                self.name = name
                break
        else:
            self.name = None

    def play(self, opponent) -> int:
        if self.name == opponent.name:
            return 3
        if opponent.name is GAME_RULES[self.name]:
            return 6
        else:
            return 0

    def __call__(self):
        return self.name.value

if __name__ == "__main__":
    with open("input.txt") as input_file:
        total = 0
        for line in input_file:
            line.strip()
            signs = line.split(" ")
            opponent = Sign(signs[0])
            me = Sign(signs[1].strip("\n"))

            total += me.play(opponent)
            total += me()

        print(f"Total points scored: {total}")

