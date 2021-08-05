""" 
    Author: Nick Tran
    Date: July 27, 2021 
    Contact Information: nick.tran@nyu.edu or 248-221-2431

    About This Program:
    ---------------------------------------------
    This is a Model of a 30-year Fixed-Rate Mortgage

    Time Complexity:    O(1), Theta(1)
    Space Complexity:   O(1), Theta(1)

    Model Limitations and Assumptions:

    1. People prepaying are only paying double their scheduled principal payment amouunt
    2. We are not considering the time period, within the month, that constitutes a prepayment
        - if someone pays 5 days before the first of the next month, would that be considered a prepayment?
        - what about paying on the first of the month?
"""

from sys import intern
from numpy.core.numeric import _ones_like_dispatcher
from numpy.testing._private.utils import nulp_diff
import numpy as np
import numpy_financial as npf #pip3 install numpy_financial and switch to base:conda environment

def scheduledAmortizedPayment(rate, nper, pv):
    """This function returns a single amortized payment,
    given the annualRate and months. rate is periodic rate"""
    pmt = npf.pmt(rate, nper, -pv)
    return (pmt)

def scheduledInterest(rate, per, nper, pv):
    """This function returns the interest payment on a given month"""
    impt = nulp_diff.ipmt(rate, per, nper, -pv)
    return impt

def scheduledPrincipal(rate, per, nper, pv):
    """This function returns the principal payment on a given month"""
    ppmt = npf.ppmt(rate, per, nper, -pv)
    return (ppmt)

class Mortgage(object):

    """This Class is used to model a single 30 year fixed rate mortgage"""

    def __init__(self, loanID, borrower, broker, period, balance, annualRate, prepaymentsArr) -> None:
        """Initialize the mortgage. Provide period in terms of months"""
        self.loanID = loanID
        self.borrower = borrower
        self.broker = broker
        self.months = [month for month in range(1, (period)+1)]
        self.period = period
        self.balance = balance
        self.periodicRate = annualRate / 12.0
        self.scheduled_AmortizedPayments = [(i, scheduledAmortizedPayment(self.periodicRate,self.period, self.balance)) \
                                                                                         for i in range(1,self.period+1)] 
        self.scheduled_PrincipalPayments = self.setScheduledPrincipalPayments(period, balance)
        self.scheduled_InterestPayments = self.setScheduledInterestPayments(period, balance)
        self.prepaidMonths = prepaymentsArr # array for designation for the month borrower prepaid
        self.maxProfit = self.calculateMaxProfit()
        self.owed = [balance]
        self.totalProfit = self.calculateInterestWithPrepayment() #Total Profit
        self.totalLoss = self.calculateTotalLoss() # Max Profit - Total Profit
        self.principal = [ppmt for month, ppmt in self.scheduled_PrincipalPayments]
        self.interest = [ipmt for month, ipmt in self.scheduled_InterestPayments]
        self.amortizedPayments = [interest + principal for interest ,principal in zip(self.interest, self.principal)]
    
    def calculateTotalLoss(self):
            return float(self.maxProfit - self.totalProfit)
        
    def calculateMaxProfit(self):
        '''This method sums the scheduled interest payments per month'''
        sum = 0
        for payment in self.scheduled_InterestPayments:
            sum += payment[1]
        return sum
    
    def setScheduledPrincipalPayments(self, nper, pv):
        '''This method sets the principal payment array'''
        tempArr = []
        for month in self.months:
            ppmt = npf.ppmt(self.periodicRate, month, nper, -pv)
            tempArr.append((month, float(ppmt)))
        return tempArr
    
    def setScheduledInterestPayments(self, nper, pv):
        '''This method sets the interest payment array'''
        tempArr = []
        balance = self.balance
        for i in range(1,self.period+1):
            ipmt = npf.ipmt(self.periodicRate, i, nper, -balance)
            tempArr.append((i, float(ipmt)))
            balance -= self.scheduled_PrincipalPayments[i-1][1]
        return tempArr

    def calculateInterestWithPrepayment(self):
        """This function returns the profit loss on a mortgage due to prepayments"""
        principal = [[month,pmt] for month, pmt in self.scheduled_PrincipalPayments]
        interest = [[month,ipmt] for month, ipmt in self.scheduled_InterestPayments]
        months = [month for month in self.prepaidMonths]
        owed = self.owed
        #if the loan has prepayments, we need to make changes to the amount of principal paid
        for i in range(1, self.period + 1):  # i = 1,2,3,...360+
        # Iterate through scheduled principal payments to find the prepaying month  
            if len(months) > 0: # if there are prepaying months:
                if months[0] == principal[i-1][0]:  # Found a prepaying month within the prepayment schedule
                    double_ppmt = principal[i-1][1] * 2
                    principal[i-1][1] = double_ppmt
                    old_balance = owed[-1]
                    new_balance = old_balance - double_ppmt
                    owed.append(new_balance) # appends the new balance
                    months.pop(0) #removes that matching month from the prepaid month list  
                    for x in range(i, self.period + 1):  # This loop updates the interest and amortized payment schedules O(360)
                        #update the interest owed and the scheduled amortized payments
                        new_interestPMT = float(npf.ipmt(self.periodicRate, x, self.period, -1 * old_balance))
                        interest[x-1][1] = new_interestPMT #updating the interest array (time series)
                        old_balance = old_balance - principal[x-1][1] #update the new balances
                else:
                    previous_balance = owed[-1]
                    owed.append(previous_balance - principal[i-1][1])
            else:
                previous_balance = owed[-1]
                owed.append(previous_balance - principal[i-1][1])

        self.interest = interest
        self.owed = owed
        return float(sum(payment for month, payment in interest))

    def __repr__(self) -> str:
        return repr("Loan ID: " + str(self.loanID) + "| Balance: " + str(self.balance) \
                  + "| Max Profit: " + str(round(self.maxProfit)) + "| Loss of Profit (from prepayments): " + str(self.totalProfit) \
                     + "| Total Loss: " + str(self.totalLoss))

def main():

    mortgage1 = Mortgage(1221130638, "Paige", "Some Broker", 360, 100000, 0.03, [2,3,4])
    mortgage2 = Mortgage(1221130638, "Ben", "A Broker", 360, 500000, 0.03, [2])
    mortgage3 = Mortgage(1221130638, "Nick", "Some Broker", 360, 100000, 0.03, [2])
    print(mortgage1)
    print(mortgage2)
    print(mortgage3)

main()


