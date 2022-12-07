def has_duplicate(l: list):
    for i1, c1 in enumerate(l):
            for c2 in l[i1+1:]:
                if c1 == c2:
                    return True

    return False



with open("input.txt", "r") as input_file:
    recieved = input_file.readline()
    window = []
    for idx, charachter in enumerate(recieved):
        window.append(charachter)
        if len(window) <= 14:
            continue
        else:
            window.pop(0)

        if not has_duplicate(window):
            print(idx+1)
            break
        

       