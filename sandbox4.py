import random




def main():

    file = open("silly.txt", 'r')
    read_file = file.readlines()
    random_line = random.choice(read_file)
    print(random_line)




def reverser():

    rev_file = open("reversable.txt", 'r')
    read_rev_file = rev_file.readlines()
    to_insert = read_rev_file[1]
    print(f"welcome to {to_insert}, Fantastic student")






#reverser()
main()