""" 
    Author: Nick Tran
    On: July 27, 2021 
    Contact: nick.tran@nyu.edu or 248-221-2431

    About This Program
    ---------------------------------------------
    This is a model of a 30-year fixed-rate loan

    Time Complexity:    O(n), Theta(1)
    Space Complexity:   O(n), Theta(1)

"""

from numpy.testing._private.utils import nulp_diff
import pandas as pd
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
        self.loss = self.calculateLoss()
        self.totalProfit = self.maxProfit - self.loss
        self.principal = []
        self.interest = []
        self.amortizedPayments = []
        self.seasonedMonths = period - len(prepaymentsArr)
        self.paid = [0.0]
        self.owed = [balance]

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
        for month in self.months:
            ipmt = npf.ipmt(self.periodicRate, month, nper, -pv)
            tempArr.append((month, float(ipmt)))
        return tempArr

    def calculateLoss(self):
        """This function returns the profit loss on a mortgage due to prepayments"""
        if len(self.prepaidMonths) > 0:
            '''we need to make changes to the amount of principal paid'''
            for prepaidMonth in self.prepaidMonths:
                index = self.scheduled_PrincipalPayments.index((prepaidMonth))
                newPrincipal = self.scheduled_PrincipalPayments[index][1] * 2

            return loss
        else:
            return 0
            
    
    def __repr__(self) -> str:
        return repr("Loan ID: " + str(self.loanID) + " Max Profit: " + str((self.maxProfit)))

def main():
    mortgage1 = Mortgage(1221130638, "Paige", "Some Broker", 360, 100000, 0.03, [])
    mortgage2 = Mortgage(1221130638, "Ben", "A Broker", 360, 500000, 0.03, [i for i in range(10,20)])
    mortgage3 = Mortgage(1221130638, "Nick", "Some Broker", 360, 100000, 0.03, [i for i in range(20,30)])
    print(mortgage1)
    print(mortgage2)
    print(mortgage3)

main()
