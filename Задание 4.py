class BankAccount:
    def __init__(self):
        self._balance = 0
        self._transactions = []

    def deposit(self, money):
        if money > 0:
            self._balance += money
            self._transactions.append(f"Пополнение: +{money}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, money):
        if 0 < money <= self._balance:
            self._balance -= money
            self._transactions.append(f"Снятие: -{money}")
        else:
            print("Недостаточно средств или неверная сумма.")

    @property
    def balance(self):
        return self._balance

    def show_transactions(self):
        print("История транзакций:")
        for b in self._transactions:
            print(b)