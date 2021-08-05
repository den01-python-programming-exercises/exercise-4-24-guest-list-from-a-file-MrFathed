def main():
    #write your code below this line
    with open("names.txt", 'r') as f:
        lines = f.read().splitlines()

    with open("other-names.txt", 'r') as f:
        lines2 = f.read().splitlines()

    names = lines + lines2
    
    print("Enter names, an empty line quits.")
    while True:
        name = input()

        if not name:
            break

        if name in names:
            print("The name is on the list")
        else:
            print("The name is not on the list")

    print("Thank you!")

if __name__ == '__main__':
    main()
