class pccafe:

    def __init__(self, name, table_num, product, price, payment):

        self.name = name
        self.table_num = table_num
        self.product = product
        self.price = price
        self.payment = payment

    def order(self):
        print("\n #주문 내역: ")

    def pay(self):
        print("\n #결제완료: ")


customer1 = pccafe("최세환", "7번-좌석", "신라면", "2500원", "현금")
customer2 = pccafe("하유민", "8번-좌석", "코카콜라", "1500원", "신용카드")
customer3 = pccafe("최민석", "9번-좌석", "묵은지삼겹볶음밥", "4500원", "현금")
customer4 = pccafe("김율희", "10번-좌석", "아메리카노", "2000원", "신용카드")

customer1.order()
print(customer1.name, customer1.table_num, customer1.product, customer1.price)

customer1.pay()
print(customer1.name, customer1.price)


customer2.order()
print(customer2.name, customer2.table_num, customer2.product, customer2.price)

customer2.pay()
print(customer2.name, customer2.price)

customer3.order()
print(customer3.name, customer3.table_num, customer3.product, customer3.price)

customer3.pay()
print(customer3.name, customer3.price)

customer4.order()
print(customer4.name, customer4.table_num, customer4.product, customer4.price)

customer4.pay()
print(customer4.name, customer4.price)
