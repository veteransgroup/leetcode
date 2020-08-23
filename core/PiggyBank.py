import string
class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100
        print(self.dollars, self.cents)

pig=PiggyBank(1,1)
pig.add_money(0,99)

password = "dr"
login={"login":"admin","password":" "}
char=(c for c in string.printable)
for i in char:
    login["password"]=password+i
    print(login.get("password"))

