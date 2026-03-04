import sys


def extract_names():
    if len(sys.argv) != 2:
        raise Exception("Invalid argument")

    input_file = sys.argv[1]

    with open(input_file, 'r') as infile, open('employees.tsv', 'w') as outfile:
        # HEADER yozish
        outfile.write("Name\tSurname\tEmail\n")

        for line in infile:
            email = line.strip()
            if not email:
                continue

            local_part = email.split('@')[0]
            name, surname = local_part.split('.')

            name = name.capitalize()
            surname = surname.capitalize()

            outfile.write(f"{name}\t{surname}\t{email}\n")


if __name__ == '__main__':
    extract_names()



#run uchun ketma-ketlik tartibi

#python3 names_extractor.py emails.txt
#python3 letter_starter.py ivan.petrov@corp.com
