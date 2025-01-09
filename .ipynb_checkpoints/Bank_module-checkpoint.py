import random as rd

def generateUniqueAccNo (allAccNo):
    acc_no = 000000000

    if len(allAccNo):
        acc_no = allAccNo[0]
    else:
        allAccNo.append(000000000)

    while acc_no in allAccNo:
        acc_no = ""
        for i in range(9):
            random_no = str(rd.randint(0, 9))
            acc_no += random_no
    
    return acc_no
    
def calculate_balance(transactions):
    balance = 0

    for transaction in transactions:
        if transaction["status"] == "active":
            if transaction["type"] == "credit":
                balance += transaction["amount"]
            else:
                balance -= transaction["amount"]

    return balance

# class Bank:
#     def __init__(self):
#         self.__admin_username = "admin"
#         self.__admin_password = "123456"

#     def auth_admin(self, username, password):
#         if self.__admin_username == username and self.__admin_password == passwrod:
#             return True
#         else:
#             False

#     @staticmethod
#     def get_all_users():
#         return BankAccount._all_accounts

# class BankAccount:
#     _all_accounts = []
    
#     def __init__(self,acc_title,acc_number,p):
#         self.__account_title = acc_title
#         self.__account_no = acc_number
#         self.__transactions = []

#         self._all_accounts.append(self)

#     def get_balance():
class Bank:
    _accounts = {}
    
    def __init__(self):
        self.__admin_username = "admin"
        self.__admin_password = "123456"
    
    # @classmethod
    def auth_admin(self, username, password):
        if self.__admin_username == username and self.__admin_password == passwrod:
            return True
        else:
            False

    # @classmethod
    def create_account (self,acc_title,acc_number):
        if not acc_title or not acc_number:
            return "Account title or number is required"

        self._accounts[acc_number] = {"title": acc_title, "transactions": []}

    # @classmethod
    def get_total_deposits(cls):
        deposits_amount = 0

        for acc in cls._accounts:
            deposit_amount = 0
            trans = cls._accounts[acc]["transactions"]
            for tran in trans:
                if tran["type"] == "credit":
                    deposit_amount+=tran["amount"]
                    
            deposits_amount+=deposit_amount

        return deposits_amount
        
    # @classmethod
    def transfer_money(cls, sender_acc_no, receiver_acc_no, amount):
        try:
            sender_acc = cls._accounts[sender_acc_no]
            sender_acc_balance = calculate_balance(sender_acc["transactions"])
            receiver_acc = cls._accounts[receiver_acc_no]

            if sender_acc_balance < amount:
                return "Sender not have sufficiant balance"

            if amount <= 0:
                return "Don`t try to steal someone money"

            sender_acc.transactions.append({
                "amount": amount,
                "type": "debit",
                "status": "active"
            })

            receiver_acc.transactions.append({
                "amount": amount,
                 "type": "credit",
                "status": "active"
            })
        except KeyError:
            return "Account not found in this acc_no"
        else:
            return "Amount send successfully"
    
    # @classmethod
    def get_account(cls, acc_no):
        try:
            cls._accounts[acc_no]
        except KeyError:
            return "Account not found in this acc_no"
        else:
            return cls._accounts[acc_no]
        
    # @classmethod
    def get_all_accounts(cls):
        return cls._accounts
    @classmethod
    def all_acc_no(cls):
        return list(cls._accounts.keys())
class BankAccount:

    @staticmethod
    def deposit(acc_no, amount):
        try:
            acc = Bank._accounts[acc_no]
            
            acc["transactions"].append({
                "amount": amount,
                "type": "credit",
                "status": "active"
            })
        except KeyError:
            return "Account not found in this acc_no"
        else:
            return "Amount deposit successfully"
            
    @staticmethod
    def withdraw(acc_no, amount):
        try:
            acc = Bank._accounts[acc_no]
            acc_balance = calculate_balance(acc["transactions"])

            if acc_balance < amount:
                return "Sender not have sufficiant balance"

            if amount <= 0:
                return "Don`t try to steal someone money"
            
            acc["transactions"].append({
                "amount": amount,
                "type": "debit",
                "status": "active"
            })
        except KeyError:
            return "Account not found in this acc_no"
        else:
            return "Amount withdraw successfully"
            
    @staticmethod
            
    def check_acc_bal(acc_no):
        try:
            acc = Bank._accounts[acc_no]
            acc_balance = calculate_balance(acc["transactions"])

            return f"Your account balance is {acc_balance}"
        except KeyError:
            return "Account not found in this acc_no"
    @staticmethod
    def print_statement(acc_no):
        try:
            acc = Bank._accounts[acc_no]
            account_transactions = acc["transactions"]
            acc_balance = calculate_balance(account_transactions)
    
            print("  Your transactions history  ")
            print("-"*29)
            for transaction in account_transactions:
                print(f"type: {transaction["type"]} | {transaction["status"]} | {transaction["amount"]}")
            print(f"Active Balance: {acc_balance}")
        except KeyError:
            return "Account is this acc_no not found"