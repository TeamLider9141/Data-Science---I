class Must_Read:
    filename = 'data.csv'

    file = open(filename, 'r')
    for line in file:
        print(line.strip())
    file.close()

if __name__ == '__main__':
    Must_Read()
