def standardPlan(age, OA, SA, payoutPlan):
    if age < 55:
        return("Minimum age is 55.")
    else:
        retirement_sum = OA + SA
        if retirement_sum >= 171000:
            if payoutPlan == "SP":
                if savingPlan == "BRS":
                    return list(map(lambda x:745, range(35)))
                elif savingPlan == "FRS":
                    return list(map(lambda x:1365, range(35)))
                elif savingPlan == "ERS" and retirement_sum >= 256500:
                    return list(map(lambda x:1985, range(35)))
        else: 
            return ("Not Enough Money")