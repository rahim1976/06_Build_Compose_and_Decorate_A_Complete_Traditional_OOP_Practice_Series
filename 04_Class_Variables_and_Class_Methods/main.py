class Bank:
    bank_name = "Global Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


account1 = Bank("Rahim")
account2 = Bank("Ali")
print(account1.bank_name)  # Global Bank
print(account2.bank_name)  # Global Bank
Bank.change_bank_name("United Bank")
print(account1.bank_name)  # United Bank
print(account2.bank_name)  # United Bank