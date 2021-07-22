class mortgage:

    def __init__(self, period, balance, rate_initial, rate_final) -> None:
        self.period = period
        self.balance = balance
        self.rate_initial = rate_initial
        self.rate_final = rate_final
        self.scheduled_Payment = []
        self.scheduled_Interest = []
        self.scheduled_Principal = []

    def scheduled_Payment(self):
        arr = []
        for i in range(30):
            payment = self.balance / self.period
            arr.append(payment)
        self.scheduled_Payment = arr
        print(arr)
    
    def get_Payment(self):
        return self.scheduled_Payment

    def __repr__(self) -> str:
        return repr(str(self.balance))

def main():
    mortgage1 = mortgage(30, 300000, 0.03, 0.03)
    print(mortgage1)

main()

