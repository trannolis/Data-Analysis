""" 
    Author: Nick Tran
    Date: August 11, 2021 
    Contact Information: nick.tran@nyu.edu or 248-221-2431

    About This Program:
    ---------------------------------------------
    This is a Model of a 30-year Fixed-Rate Mortgage Pool

    Time Complexity:    O(n(360*360)), Theta(n)
    Space Complexity:   O(n), Theta(n)

    Model Limitations and Assumptions:

    1. People prepaying are only paying double their scheduled principal payment amouunt
    2. We are not considering the time period, within the month, that constitutes a prepayment
        - if someone pays 5 days before the first of the next month, would that be considered a prepayment?
        - what about paying on the first of the month?
"""

from mortgage import Mortgage

class Pool(object):
    '''This class models a 30 Year MBS Pool'''
    def __init__(self) -> None:
        '''Initiates Attributes of a Pool'''
        self.mortgages = {} #Dictionary to Store the Loans in the Pool
        self.total_balance = 0.0
        self.totalPrepaidAmount = 0.0
        self.unpaidPrincipal = 0.0
        self.maximumProfit = 0.0
        self.totalLoss = 0.0
        self.CPR = 0.0
        self.noteRate = 0.0
        self.historicalCPR = [] #records the historical CPR on the pool

    def setTotalBalance(self):
        '''Sets the total balance of a Pool'''
        ...

    def calculateTotalUnpaidBalance(self):
        ...

    def addLoan(self, aMortgage):
        '''Add a Loan to the Pool'''
        ...
    
    def setSMM(self):
        '''Helper Function for CPR: Returns the Single-Monthly-Mortality-Rate of a Pool'''
        ...

    def setCPR(self):
        '''Sets the CPR on the Pool'''
        ...
    
    def setWAM(self):
        '''Sets the Weighted-Average-Maturity on a Pool'''

    def setWAL(self):
        '''Sets the Weighted-Average-Life of a Pool'''
        ...
    
    def setWAC(self):
        '''Sets the Weighted-Average-Coupon Rate of a Pool'''
        ...
    
    def setTotalLoss(self):
        '''Sets the total Loss on a Pool'''
        ...
    
    def default(self, defaultedMortgage):
        '''Removes mortgage and recalculates Pool Figures'''
        self.calculateCPR()
        self.calculateSMM()
        self.calculateWAC()
        self.calculateWAL()
        self.calculateTotalLoss()
        return True
    
    def removeMortgage(self, delMortgage):
        # https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary
        del self.mortgages[delMortgage.Loan_ID] #removes the mortgage from the dictionary
        return True
    
    def __repr__(self) -> str:
        return ...

