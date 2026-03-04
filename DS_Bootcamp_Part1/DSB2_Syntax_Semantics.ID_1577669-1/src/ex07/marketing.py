import sys


def marketing():
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
    ]

    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'
    ]

    recipients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
    ]

    if len(sys.argv) != 2:
        raise Exception("Invalid argument")

    task = sys.argv[1]

    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)

    if task == "call_center":
        result = clients_set - recipients_set

    elif task == "potential_clients":
        result = participants_set - clients_set

    elif task == "loyalty_program":
        result = clients_set - participants_set

    else:
        raise Exception("Invalid argument")

    for email in result:
        print(email)


if __name__ == '__main__':
    marketing()
