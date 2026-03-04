import sys
import os


class Research:
        def __init__(self, file_path):

            if not os.path.exists(file_path):
                raise Exception("File does not exist")
            self.file_path = file_path

        def file_reader(self):
            with open(self.file_path, 'r') as f:
                lines = f.read().strip().split('\n')

            header = lines[0].split(',')
            if len(header) != 2:
                raise Exception("Invalid file structure")


            for line in lines[1:]:
                values = line.split(',')
                if values not in [['0', '1'], ['1', '0']]:
                    raise Exception("Invalid file structure")

            return '\n'.join(lines)


def main():
    if len(sys.argv) != 2:
        raise Exception("Wrong number of arguments")

    research = Research(sys.argv[1])
    print(research.file_reader())


if __name__ == '__main__':
    main()
