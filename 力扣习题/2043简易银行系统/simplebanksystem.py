from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.bal = balance
        self.n = len(self.bal)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n or account2 < 1 or account2 > self.n:
            return False
        if self.bal[account1 - 1] >= money:
            self.bal[account1 - 1] -= money
            self.bal[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        if self.bal[account - 1] < money:
            return False
        else:
            self.bal[account - 1] -= money
            return True


# Your Bank object will be instantiated and called as such:

b = [10, 100, 20, 50, 30]
obj = Bank(b)
print(obj.withdraw(3, 10))
print(obj.transfer(5, 1, 20))
print(obj.deposit(5, 20))
print(obj.transfer(3, 4, 15))
print(obj.withdraw(10, 50))
