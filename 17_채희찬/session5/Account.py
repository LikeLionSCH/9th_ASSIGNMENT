class Account:
    def __init__(self, name, password, money):
        self.name = name
        self.password = password
        self.money = money
    
    # 출금
    def withdrawal(self):
        if (input("이름을 입력하시오: "))==self.name and (input("비밀번호를 입력하시오: "))==self.password:     # 이름과 비밀번호가 일치할 경우
            while(True):
                withdrawal_money = int(input("출금할 금액을 입력하시오: "))
                if withdrawal_money <= self.money:      # 출금액이 잔액보다 작거나 같을 경우
                    print("출금이 완료되었습니다.\n통장과 현금을 가져가세요.")
                    self.sub_money(withdrawal_money)
                    self.check_balance()
                    break
                else:       # 출금액이 잔액보다 클 경우
                    print("잔액이 부족합니다.")
                    self.check_balance()
        else:       # 이름과 비밀번호가 일치하지 않을 경우
            print("이름이나 비밀번호가 다릅니다.")

    # 입금
    def deposit(self):
        deposit_money = int(input("예금할 금액을 입력하시오: "))
        print("예금이 완료되었습니다.\n통장을 가져가세요.")
        self.add_money(deposit_money)
        self.check_balance()

    # 감액
    def sub_money(self, withdrawal_money):
        self.money -= withdrawal_money

    # 가액
    def add_money(self, deposit_money):
        self.money += deposit_money
    
    # 잔액조회
    def check_balance(self):
        print(f"잔액은 {self.money}원 입니다.\n=====================")
    
    
chae = Account("chae", "1234", 5000)
chae.withdrawal()
chae.deposit()