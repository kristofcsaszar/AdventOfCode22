from rucksack import get_letter_priority
from collections import Counter

def get_badge(group):
    tallied = []
    for inventory in group:
        tallied.append(Counter(inventory))


    for key in tallied[0].keys():
        for others_inventory in tallied[1:]:
            if key not in others_inventory:
                break
        else:
            return key

def print_results(group, badge):
    print("For group")
    res = ""
    for g in group:
        res+= ("\t" + g)
    print(res)
    print(f"Found badge: {badge}")

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        group = []
        badge_prio_total = 0
        for line in input_file:
            group.append(line)
            if len(group) == 3:
                badge = get_badge(group)
                # print_results(group, badge)
                badge_prio_total += get_letter_priority(badge)
                # reset group to empty 
                group = []

        print(badge_prio_total)
