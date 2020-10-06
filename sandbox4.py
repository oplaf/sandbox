def main():

    file = open("silly.txt", 'r')
    read_file = file.readlines()
    for line in read_file:
        print(line)



def reverser():

    rev_file = open("reversable.txt", 'r')
    read_rev_file = rev_file.readlines()
    to_insert = read_rev_file[1]
    print(f"welcome to {to_insert}, Fantastic student")






#reverser()
main()