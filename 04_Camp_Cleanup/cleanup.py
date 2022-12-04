class Range:
    def __init__(self, string: str):
        split = string.split("-")
        self.start = int(split[0])
        self.end = int(split[1])

    def contains(self, other) -> bool:
        if self.end - other.end >= 0:
            if other.start - self.start >= 0:
                return True
        return False

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        count = 0
        for line in input_file:
            split = line.split(",")
            range1 = Range(split[0])
            range2 = Range(split[1])

            if range1.contains(range2) or range2.contains(range1):
                count+=1

        print(count)
