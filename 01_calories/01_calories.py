class FixedTopQueue:
    """
    This class accepts inputs, and only keeps the top n

    @param: size: specifies the number of max items

    """
    def __init__(self, size:int) -> None:
        self.size = size
        self.list = []

    def push(self, number):
        if len(self.list) < self.size:
            self.list.append(number)
        else:
            min_list = min(self.list)
            if number > min_list:
                self.list.remove(min_list)
                self.list.append(number)

    def total(self):
        return sum(self.list)


if __name__ == "__main__":
    input_file = open("input.txt", "r")


    top_three = FixedTopQueue(3)
    total = 0


    for line in input_file:
        # jump to new elf
        if line == "\n":
            top_three.push(total)
            total = 0
        else:
            total+= int(line)

    print(f"The top 3 elf carrying the most has {top_three.total()} calories.")
           

        