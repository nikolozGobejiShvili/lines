import sys

try:
    if len(sys.argv) == 1:
        sys.exit("too few  commnad-line argument")
    if len(sys.argv) > 2:
        sys.exit("too many command-line argument")
    if sys.argv[1].split(".")[1] != "py":
        sys.exit("not a python file")
    else:
        with open (sys.argv[1]) as file:
            count = 0
            for line in file:
                line = line
                if line[0] != "#":
                    count += 1 
                elif line == "":
                    continue 
        print("lines: " + str(count))

except FileNotFoundError:
    print("file doesnt  exist")
    
