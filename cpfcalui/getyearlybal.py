from datetime import datetime
import pandas as pd

COLUMN_NAMES = ['Age', 'OA', 'SA', 'Medi']
int_OA = 0.025
int_SA = 0.04
int_Medi = 0.04

class person(object):
    def __init__(self, curr_age, curr_OA, curr_SA, curr_Medi,yearly_contri,  topup, hdb_mth, hdb_amt, *args):
        self.curr_age = curr_age
        self.curr_OA = curr_OA # during the december of the previous year
        self.curr_SA = curr_SA # during the december of the previous year
        self.curr_Medi = curr_Medi
        self.topup = topup
        self.hdb_mth = hdb_mth
        self.hdb_amt = hdb_amt
        self.yearly_bal = pd.DataFrame(columns=COLUMN_NAMES)
        self.yearly_contri = yearly_contri
        
    # dummy function
    def make_contri(self):
        age = self.curr_age
        yearly_contri = self.yearly_contri
        while age <= 55:
            yearly_contri = yearly_contri.append({'Age':age,'OA':10000,'SA':5000,'Medi':5000},ignore_index=True)
            age +=1
        self.yearly_contri = yearly_contri
        print(yearly_contri)


    def get_yearly_bal(self):
        
        age = self.curr_age
        OA = self.curr_OA
        SA = self.curr_SA
        topupAmt = self.topup
        Medi = self.curr_Medi
        yearly_bal = self.yearly_bal
        yearly_contri = self.yearly_contri
        # display(yearly_contri)
        curr_mth = datetime.now().month
        hdb_mth = self.hdb_mth
        hdb_amt = self.hdb_amt
        yearly_contri = yearly_contri.set_index(['Age'])
        int = 0
        while age <= 55:
            remain_mth = 13-curr_mth # catch initial remaining months depending on date of calculation
            curr_mth = 1 # reset current month to count from the start of each year
            paying_mth = min(hdb_mth,remain_mth,12) # determine no. of months of hdb loan payment in the current year of iteration
            hdb_mth = hdb_mth-paying_mth # determine total no. of months left for payment
            
            # (balance + contribution - any loan payment)*(1 + interest rate)
            OA = (OA+yearly_contri.loc[age]['Ordinary']+topupAmt-(paying_mth*hdb_amt))*(1+int_OA) 
            SA = (SA+yearly_contri.loc[age]['Special'])*(1+int_SA)+topupAmt
            Medi = (Medi+yearly_contri.loc[age]['Medisave'])*(1+int_Medi)+topupAmt
            yearly_bal = yearly_bal.append({'Age': age,'OA': OA,'SA': SA, 'Medi': Medi} ,ignore_index=True)
            age += 1
            int += 1
        self.yearly_bal = yearly_bal 
        return yearly_bal
        # display(self.yearlybal)

if __name__== "__main__":
    # to test
    a = person(40,0,0,0)
    a.get_yearly_bal()
    print(a.yearly_bal)