    
if __name__ == "__main__":
    input_file = open("input.txt", "r")

    max_total = 0
    total = 0


    for line in input_file:
        # jump to new elf
        if line == "\n":
            if total>=max_total:
                max_total = total
            total = 0
        else:
            total+= int(line)

    print(f"The elf carrying the most has {max_total} calories.")
           

        