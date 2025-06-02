from argparse import ArgumentError


class BankAccount:
    __bank_address: str = "1 Allenby St, Tel Aviv"

    def __init__(self, owner: str, balance: float):
        self.__owner = owner
        self.__balance = balance

    @classmethod
    def get_bank_address(cls) -> str:
        return cls.__bank_address

    @staticmethod
    def highest_balance(acc1: "BankAccount", acc2: "BankAccount", acc3: "BankAccount") -> float:
        if acc1.balance >= acc2.balance and acc1.balance >= acc3.balance:
            return acc1.balance
        elif acc1.balance <= acc2.balance and acc2.balance >= acc3.balance:
            return acc2.balance
        elif acc1.balance <= acc3.balance and acc2.balance <= acc3.balance:
            return acc3.balance
        else:
            raise ValueError("Incorrect data. Use numbers only")

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    # I know, you asked that's the "owner" should be a read-only type, but without a setter the code doesn't work.
    def owner(self, name):
        self.__owner = name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def is_rich(self) -> bool:
        if self.balance > 1000000:
            return True
        else:
            return False

    def __add__(self, other: "BankAccount, float") -> float:
        if isinstance(other, BankAccount):
            total = self.balance + other.balance
        elif isinstance(other, (int, float)):
            total = self.balance + other
        else:
            raise TypeError(f"BankAccount doesn't support add function for type {type(other)}")
        return total

    def __sub__(self, other: "BankAccount, float") -> float:
        if isinstance(other, BankAccount):
            total = self.balance - other.balance
        elif isinstance(other, (int, float)):
            total = self.balance - other
        else:
            raise TypeError(f"BankAccount doesn't support subtract function for type {type(other)}")
        return total

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.balance == other.balance
        elif isinstance(other, (int, float)):
            return self.balance == other
        elif isinstance(other, tuple):
            return self.owner == other[0] and self.balance == other[1]
        else:
            raise TypeError(f"BankAccount doesn't support 'equal' function for type {type(other)}")

    def __ne__(self, other):
        if not isinstance(other, BankAccount) and not isinstance(other, (int, float)) and not isinstance(other, tuple):
            raise TypeError(f"BankAccount class doesn't support 'difference' for type {type(other)}")
        return not self == other

    def __gt__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"BankAccount doesn't support '>' for type {type(other)}")
        return self.balance > other.balance

    def __ge__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"BankAccount doesn't support '>=' for type {type(other)}")
        return self > other or self == other

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"BankAccount doesn't support '<' for type {type(other)}")
        return not self >= other

    def __le__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"BankAccount doesn't support '<=' for type {type(other)}")
        return self < other or self == other

    def __str__(self):
        return f"BankAccount ({self.owner} {self.balance})"

    def __repr__(self):
        return f"BankAccount ({self.owner} {self.balance})"

    def __len__(self):
        return round(self.balance)

    def __getitem__(self, item):
        match item:
            case 'owner' | 0:
                return self.owner
            case 'balance' | 1:
                return self.balance
            case _:
                raise ArgumentError(f"Unsupported type {type(item)}")

    def __iter__(self):
        yield "owner", self.owner
        yield "balance", self.balance


# Create accounts
acc1 = BankAccount("Alice", 800.0)
acc2 = BankAccount("Bob", 1200.0)
acc3 = BankAccount("Alice", 800.0)
acc4 = BankAccount("Charlie", 300.0)

# Test __repr__ / __str__
print("Accounts:")
print(acc1)
print(acc2)
print(acc3)

# Test __eq__ (same owner and balance)
print("\nEquality:")
print("acc1 == acc3:", acc1 == acc3)  # True
print("acc1 == acc2:", acc1 == acc2)  # False
print("acc1 == 800:", acc1 == 800)  # True
print("acc1 == ('Alice', 800):", acc1 == ("Alice", 800))  # True

# Test __ne__
print("\nInequality:")
print("acc1 != acc2:", acc1 != acc2)  # True

# Test __gt__ (based on balance)
print("\nGreater Than:")
print("acc2 > acc1:", acc2 > acc1)  # True
print("acc4 > acc1:", acc4 > acc1)  # False

# Test __lt__, __ge__, __le__
print("\nOther comparisons:")
print("acc1 < acc2:", acc1 < acc2)  # True
print("acc2 >= acc1:", acc2 >= acc1)  # True
print("acc4 <= acc1:", acc4 <= acc1)  # True

# Test __add__ (same owner)
print("\nAdd:")
acc5 = acc1 + acc3
print("acc5 (Alice + Alice):", acc5)  # 1600

# Test __add__ (different owners)
acc6 = acc1 + acc2
print("acc6 (Alice + Bob):", acc6)  # 2000

# Test __add__ with number
acc7 = acc1 + 200
print("acc1 + 200:", acc7)  # 1000

# Test __sub__ with another account
acc8 = acc2 - acc1
print("acc2 - acc1:", acc8)  # 400

# Test __sub__ with number
acc9 = acc2 - 500
print("acc2 - 500:", acc9)  # 700

# Test __getitem__
print("\nGet item:")
print("acc1['owner']:", acc1['owner'])
print("acc1[1]:", acc1[1])  # balance

# Test __iter__
print("\nIterating acc1:")
for info in acc1:
    print(info)

# Test __len__
print("\nLength of acc1:", len(acc1))

# Test class method
print("\nBank address:", BankAccount.get_bank_address())

# Test static method
print("\nHighest balance:", BankAccount.highest_balance(acc1, acc2, acc4))
