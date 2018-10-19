import sys

def rememberer(thing):
    # LONG WAY
    # open file
    #file = open("database.txt", "a")
    # write things to file
    #file.write(thing+"\n")
    # close file
    #file.close()
    #pass
    with open("database.txt", "a") as file:
        file.write(thing+"\n")


def show():
    # open file
    with open("database.txt") as file:
        # print out each line in file
        for line in file:
            print(line)
    # close file
    pass

if __name__ == "__main__":
    # sys.argv is all the arguments after filename
    # python remember.py juice boxes
    #        argv0       argv1 argv2
    if sys.argv[1].lower() == '--list':
        show()
    rememberer(' '.join(sys.argv[1:]))