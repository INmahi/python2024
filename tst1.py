import sys

def main():
    try:
        file = sys.argv[1]
        if len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        if not file.lower().endswith(".py"):
            sys.exit("Not a Python file")
        print(get_lines(file))
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

def get_lines(file):
    valid_lines = []
    with open(file,"r") as f:
        all_lines = f.readlines()
        for l in all_lines:
            l = l.strip()
            if not l.startswith("#") and not l == "":
                valid_lines.append(l)
                
    return len(valid_lines)


main()