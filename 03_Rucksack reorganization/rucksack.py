def find_outlier(string1: str, string2: str):
    already_checked = set()
    for char1 in string1:
        # don't check anything for outlier twice
        if char1 in already_checked:
            continue
        else:
            already_checked.add(char1)
        
        for char2 in string2:
            # if the same, found the outlier
            if char1 == char2:
                return char2

def get_letter_priority(letter: chr) -> int:
    ascii = ord(letter)
    # priority of lower case letters is calculated like this
    lower_case_prio = ascii -96
    # if result non-positive, wasn't lower case
    if (lower_case_prio) > 0:
        return lower_case_prio
    else:
        return lower_case_prio + 58

if __name__ == "__main__":
    priority_sum = 0

    with open("input.txt", "r") as input_file:
        for line in input_file:
            l = int(len(line) / 2)
            priority_sum += get_letter_priority(find_outlier(line[:l], line[l:]))

    print(priority_sum)

