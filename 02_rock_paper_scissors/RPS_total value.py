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

def calculateOwnSign(opponent: Sign, outcome)-> Sign:
    ownSign = Sign("X")
    match outcome:
        # need to lose
        case "X":
            ownSign.name = GAME_RULES[opponent.name]
        # draw
        case "Y":
            ownSign.name = opponent.name
        # need to win
        case "Z":
            for winner, loser  in GAME_RULES.items():
                if opponent.name is loser:
                    ownSign.name = winner

    return ownSign


if __name__ == "__main__":
    with open("input.txt") as input_file:
        total = 0
        for line in input_file:
            signs = line.split(" ")
            opponent = Sign(signs[0])

            # call for Pt1:
            # me = Sign(signs[1].strip("\n"))
            # call for Pt2:
            me = calculateOwnSign(opponent, signs[1].strip("\n"))

            total += me.play(opponent)
            total += me()

        print(f"Total points scored: {total}")

