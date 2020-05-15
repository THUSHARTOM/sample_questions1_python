#Program to manage bank account and amount deposited and withdrawn from bank

class Account:

    def __init__(self, num, strin, bal):
        self.account_no = num
        self.account_name = strin
        self.account_balance = bal

    def depositAmnt(self,amnt_deposited):
        self.account_balance = self.account_balance + amnt_deposited

    def withdrawAmnt(self,amnt_withdrawn):
        if self.account_balance >= amnt_withdrawn:
            self.account_balance = int(self.account_balance) - int(amnt_withdrawn)
            if self.account_balance >= 1000:
                return 1
        else:
            return 0

if __name__ == "__main__":
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())
    acnt = Account(acno,acname,acntbal)
    acnt.depositAmnt(depamnt)
    print(acnt.account_balance)
    res = acnt.withdrawAmnt(withamnt)
    if res == 1 :
        print(acnt.account_balance)
    else:
        print("Insufficient balance for withdrawal")



