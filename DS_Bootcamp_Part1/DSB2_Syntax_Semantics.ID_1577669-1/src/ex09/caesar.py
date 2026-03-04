import sys


def caesar():
    if len(sys.argv) != 4:
        raise Exception("Invalid arguments")

    mode = sys.argv[1]
    text = sys.argv[2]
    shift = sys.argv[3]

    if not shift.isdigit():
        raise Exception("Invalid arguments")

    shift = int(shift)

    if mode not in ["encode", "decode"]:
        raise Exception("Invalid arguments")

    # Cyrillic check
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            raise Exception("The script does not support your language yet.")

    if mode == "decode":
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    print(result)


if __name__ == '__main__':
    caesar()

#shifrlash => python3 caesar.py encode 'salom3' 1  => natijam => tbmpn3
#deshifrlash => python3 caesar.py decode 'tbmpn3' 1  => natija => salom3
