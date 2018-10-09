import numpy as np
import pandas as pd
from datetime import datetime


## contribution_table gives the contribution of employer to employee's cpf accounts according to employee's age
def contribution_table():
	d = {'Age': [35,36,46,51,56,61,66], 
	'Ordinary': [0.23, 0.21,0.19,0.15,0.12,0.035,0.01],
	'Special': [0.06, 0.07,0.08,0.115,0.035,0.025,0.01],
	'Medisave': [0.08, 0.09,0.1,0.105,0.105,0.105,0.105]}
	
	df = pd.DataFrame(data=d)

	return df

## To do the calculation for contribution to each account for each year 
def calculation(salary,num_months,contribution_o,contribution_s,contribution_m):
	
	ordinary=int(salary*num_months*contribution_o)
	special=int(salary*num_months*contribution_s)
	medisave=int(salary*num_months*contribution_m)

	return ordinary,special,medisave

## calculate_each_account gives the contribution to each account according to the salary at the respective age
def calculate_each_account(df):


	# To retrieve the contribution table
	contribution_percentage=contribution_table()

	# To initialize an empty dataframe for the final output
	final_contribution = pd.DataFrame()

	# To iterate through every age in the dataframe keyed in by the user
	for i in range (len(df['Age'])):

		num_months=12

		if(i==0):
			num_months=num_months-datetime.now().month

		df['Age'][i]=int(df['Age'][i])

		# To retrieve the first age in the data frame that's larger than or equal to the age concerned
		first_largest_age=next(row['Age'] for index, row in contribution_percentage.iterrows() if row['Age'] >= df['Age'][i])
		first_largest_age=int(first_largest_age)

		# To retrieve corresponding percentages for the corresponding age
		index_first_largest_age=contribution_percentage[contribution_percentage['Age']==first_largest_age].index.item()
		difference=1

		if(df['Age'][i]<first_largest_age):
		
			if(i!=len(df['Age'])-1):
				difference=int(df['Age'][i+1])-df['Age'][i]

			if(index_first_largest_age!=0):
				index_first_largest_age-=1

		# To calculate the corresponding absolute amount contributed to each account for the first year
		salary=int(df['Salary'][index_first_largest_age])
		ordinary,special,medisave=calculation(salary,num_months,contribution_percentage.loc[[index_first_largest_age]]['Ordinary'].values[0],
			contribution_percentage.loc[[index_first_largest_age]]['Special'].values[0],
			contribution_percentage.loc[[index_first_largest_age]]['Medisave'].values[0])
		starting_age=int(df['Age'][i])
		final_contribution= final_contribution.append({'Age': starting_age, 'Ordinary': ordinary, 'Special': special,'Medisave':medisave}, ignore_index=True)

		# To calculate the corresponding absolute amount contributed to each account for the subsequent years after the first year
		num_months=12
		ordinary,special,medisave=calculation(salary,num_months,contribution_percentage.loc[[index_first_largest_age]]['Ordinary'].values[0],
			contribution_percentage.loc[[index_first_largest_age]]['Special'].values[0],
			contribution_percentage.loc[[index_first_largest_age]]['Medisave'].values[0])


		# To append the calculated amount for each account to the dataframe
		for i in range(1,difference):
				starting_age+=1
				final_contribution= final_contribution.append({'Age': starting_age, 'Ordinary': ordinary, 'Special': special,'Medisave':medisave}, ignore_index=True)
			
	print(final_contribution)
	return(final_contribution)
	
if __name__== "__main__":

	today = datetime.today()
	datem = datetime(today.year, today.month, 1)
	currentMonth = datetime.now().month
	print(currentMonth)
	# To test the code
	d = {'Age': [34, 45], 'Salary': [3000, 4000]}
	df = pd.DataFrame(data=d)
	calculate_each_account(df)