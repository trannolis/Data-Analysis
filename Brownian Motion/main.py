import pandas as pd
import numpy as np
import numpy_financial as npf
from datetime import date

def scheduledAmortizedPayment(rate, nper, pv):
    """This function returns a single amortized payment,
    given the annualRate and months."""
    if rate!=0:
        pmt = (rate*(pv*(1+ rate)**nper))/((1+rate) * (1-(1+ rate)**nper))
    else:
        pmt = (-1*(pv)/nper)  
    return -(pmt)

def scheduledInterest(rate, per, nper,pv):
    ipmt = -( ((1 + rate)**(per-1)) * (pv*rate + scheduledPrincipal(rate, per, nper, pv)) - scheduledAmortizedPayment(rate, nper, pv))
    return(ipmt)

def scheduledPrincipal(rate, per, nper, pv):
    """This function returns the principal payment on a given month"""
    ppmt = scheduledAmortizedPayment(rate, nper, pv) - scheduledInterest(rate, per, nper, pv)
    return(ppmt)

class Mortgage(object):
    def __init__(self, loanID, borrower, broker, period, balance, annualRate, prepaymentsArr) -> None:
        """Initialize the mortgage. Provide period in terms of months"""
        self.loanID = loanID
        self.borrower = borrower
        self.broker = broker
        self.period = period
        self.balance = balance
        self.periodicRate = annualRate / 12.0
        self.payment = scheduledAmortizedPayment(balance, self.periodicRate, period)
        self.scheduled_AmortizedPayments = [scheduledAmortizedPayment(self.periodicRate, self.period, self.balance) for i in range(self.period)] 
        #self.scheduled_PrincipalPayments = scheduledAmortizedPayment(balance, self.periodicRate, period)
        #self.scheduled_InterestPayments = scheduledInterest(self.scheduled_AmortizedPayments, self.scheduled_PrincipalPayments)
        self.prepaidMonths = self.prepayments(prepaymentsArr) # array for designation for the month borrower prepaid
        self.paid = [0.0] # list of all payments made towards the loan
        self.owed = [balance] #list of balances after every month
    
    def prepayments(self, prepaymentsArr):
        """Method sets the prepayment schedule"""
        if len(prepaymentsArr) > 0:
            self.prepaidMonths = prepaymentsArr
            #self.calculateLoss(prepaymentsArr)
        else:
            self.prepaidMonths = []
        return 1

    def calculateLoss():
        """This function returns the profit loss on a mortgage due to prepayments"""
        
        return 1
    
    def calculateProfit():
        return 1
    
    def __repr__(self) -> str:
        return repr(str(len(self.scheduled_AmortizedPayments)))

def main():
    mortgage1 = Mortgage(1221130638, "Paige", "Some Broker", 360, 500000, 0.03, [1,2,3])
    mortgage2 = Mortgage(1221130638, "Ben", "A Broker", 360, 500000, 0.03, [i for i in range(10,20)])
    mortgage3 = Mortgage(1221130638, "Nick", "Some Broker", 360, 500000, 0.03, [i for i in range(20,30)])
    print(mortgage1)
    print(mortgage2)
    print(mortgage3)

main()

def main2():
    balance = 100000
    rate = 0.03 / 12
    month = 3
    months = 360
    #print(str(scheduledAmortizedPayment(rate, months, balance)))
    #print(str(scheduledPrincipal(rate, month, months, balance)))
    principal = 10000.00
    per = np.arange(1*12) + 1 # The 'per' variable represents the periods of the loan. Remember that financial equations start the period count at 1!
    ipmt = npf.ipmt(0.0850/12, per, 1*12, principal)
    interestpd = np.sum(ipmt)
    print(np.round(interestpd, 3))


main2()