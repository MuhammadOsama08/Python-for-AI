class BankAccount:
    bank_name = "HBL"          # class attribute - shared by all accounts
    total_accounts = 0         # shared counter

    def __init__(self, owner, balance=0):
        self.owner = owner     # instance attribute - one per object
        self.balance = balance
        BankAccount.total_accounts += 1   # bump the shared counter


    def transfer(self, receiver, amount):
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return

        if amount > self.balance:
            print(f"{self.owner} does not have enough balance.")
            return

        self.balance -= amount
        receiver.balance += amount
        print(f"{amount} transferred from {self.owner} to {receiver.owner}.")

ali = BankAccount("Ali", 5000)
zara = BankAccount("Zara", 3000)

print(ali.bank_name, "-", zara.bank_name)        # both see the same shared value
print("Accounts opened:", BankAccount.total_accounts)

ali.transfer(zara, 2000)
print("Ali's balance:", ali.balance)
print("Zara's balance:", zara.balance)
