import sys


def start_letter():
    if len(sys.argv) != 2:
        raise Exception("Invalid argument")

    target_email = sys.argv[1]

    with open('employees.tsv', 'r') as file:
        next(file)  # header skip qilish

        for line in file:
            name, surname, email = line.strip().split('\t')

            if email == target_email:
                print(f"Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                return

    raise Exception("Email not found")


if __name__ == '__main__':
    start_letter()


#run uchun ketma-ketlik tartibi

#python3 names_extractor.py emails.txt
#python3 letter_starter.py ivan.petrov@corp.com
