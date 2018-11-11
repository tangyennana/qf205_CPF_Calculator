def basic_plan(age,oa,sa,sum_type):
	#only for age 55 and above!
    if age<55:
        return("Minimum age is 55.")
	
	# checking if user is eligible for the plan and also assigning payout to it using an if else statement.
    if sum_type =="BRS":
        if oa+sa<171000 :
            return ("Not Enough Money")
        else:
            return list(map(lambda x:790, range(35))) 
    elif sum_type == "FRS":
	    if oa+sa<171000 :
		    return ("Not Enough Money")
	    else:
		    return list(map(lambda x:1265, range(35))) 
    else:
	    if oa+sa<256500 :
		    return ("Not Enough Money")
	    else:
		    return list(map(lambda x:1840, range(35))) 
			
			
			
