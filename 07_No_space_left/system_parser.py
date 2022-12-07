import regex_spm

class SystemElement:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
    
    def get_size(self):
        raise NotImplementedError("This is an abstract class")

class File(SystemElement):
    def __init__(self, name, size) -> None:
        super().__init__(name)
        self.size = size

    def get_size(self):
        return  self.size

class Directory(SystemElement):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.contained_elements = []

    def add(self, element:SystemElement):
        element.parent = self
        self.contained_elements.append(element)
        

    def get_size(self):
        sum = 0
        for e in self.contained_elements:
            sum += e.get_size()

        return sum

if __name__ == "__main__":
    cwd = Directory("/")
    all_dirs = set()
    all_dirs.add(cwd)

    with open("input.txt", "r") as input_file:
        all_lines = input_file.readlines()
        for line in all_lines[1:]:
            match regex_spm.match_in(line):
                case r"\$ cd [a-z]+":
                    # stepping into a directory
                    split = line.split(" ")
                    for d in cwd.contained_elements:
                        if split[2] == d.name:
                            cwd = d
                            break
                    else:
                        raise ValueError(f"{split[2]} not in {cwd}")

                case r"\$ cd ..":
                    # stepping out of directory
                    cwd = cwd.parent

                case r'\d+ [a-z]+(.[a-z]+)?':
                    # this is a file
                    split = line.split(" ")
                    cwd.add(File(name = split[1], size = int(split[0])))

                case r'dir [a-z]+':
                    # this is a directory
                    split = line.split(" ")
                    dir = Directory(split[1])
                    all_dirs.add(dir)
                    cwd.add(dir)

                case r'\$ ls':
                    # ls command, don't care, only parse results
                    pass
                case _:
                    print(f"This line didn't match anything: {line}")

    print(f"Parsing done, {len(all_dirs)} directories found.")
    # parsing done
    total_sub_100_000_size = 0
    for dir in all_dirs:
        current_size = dir.get_size()
        if current_size <= 100_000:
            total_sub_100_000_size += current_size

    print(f"Total size of all sub 100 000 direcotries is {total_sub_100_000_size}")