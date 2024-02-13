class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES Sent to {recipient} successfully")
        else:
            print("Insufficient balance")


class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buyairtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfully")
        else:
            print("Insufficient balance")


class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receive_money(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received successfully")


personal = Personal_Mpesa(500, 713250319, 29100741)
personal.send_money(400, 713250319)
personal.buyairtime(850)
business = Business_Mpesa(500, 73424566, "martin")
business.receive_money(500)
