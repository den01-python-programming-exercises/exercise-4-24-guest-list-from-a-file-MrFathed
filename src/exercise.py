def main():
    #write your code below this line
    file_name = input("Name of the file:")

    with open(file_name, 'r') as f:
        names = f.read().splitlines()
    
    while True:
        name = input("Enter names, an empty line quits.")

        if not name:
            break

        if name in names:
            print("The name is on the list.")
        else:
            print("The name is not on the list.")

    print("Thank you!")

if __name__ == '__main__':
    main()
