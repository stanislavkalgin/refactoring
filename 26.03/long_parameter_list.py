# before
def hard_bank_decision(clients_balance, clients_income, clients_age,
                       clients_reputation, key_rate, banks_interest):
    if clients_balance <= 0:
        if clients_reputation <= 0:
            send_angry_letter()
        else:
            send_sad_letter()

    else:
        if clients_age >= 21:
            if clients_income >= 35_000:
                send_advertising_letter(clients_income, key_rate, banks_interest)


clients_balance = client_245.get_balance()
clients_income = client_245.get_income()
clients_age = client_245.get_age()
clients_reputation = client_245.get_reputation()

hard_bank_decision(clients_balance, clients_income, clients_age,
                   clients_reputation, current_key_rate, current_bank_interest)


# after
def hard_bank_decision(client, key_rate, banks_interest):
    if client.get_balance() <= 0:
        if client.get_reputation() <= 0:
            send_angry_letter()
        else:
            send_sad_letter()

    else:
        if client.get_age() >= 21:
            if client.get_income() >= 35_000:
                send_advertising_letter(client.get_income(), key_rate, banks_interest)


hard_bank_decision(client_245, current_key_rate, current_bank_interest)
