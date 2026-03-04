class Research:
    def file_reader(self):
        file = open('data.csv', 'r')
        data = file.read()
        file.close()
        return data


if __name__ == '__main__':
    research = Research()
    print(research.file_reader())
