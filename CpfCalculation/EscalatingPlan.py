def escalatingPlan(age, package, oa, sa):
    
    #Not eligible for age less than 55
    if age < 55:
        return("Minimum age is 55.")
  
    #Loop through 65 to 100 years old
    #Compound 2% interest to initial amount yearly
    #Based on retirement package and amount
    if package == "BRS" and (oa+sa) >= 85500:
        dataPoints = []
        monthlyPayout = 418.5
        dataPoints.append(monthlyPayout)
        for x in range(34):
            monthlyPayout = monthlyPayout*(102/100)
            dataPoints.append(monthlyPayout)
        return dataPoints
  
    if package == "FRS" and (oa+sa) >= 171000:
        dataPoints = []
        monthlyPayout = 777.5
        dataPoints.append(monthlyPayout)
        for x in range(34):
            monthlyPayout = monthlyPayout*(102/100)
            dataPoints.append(monthlyPayout)
        return dataPoints
  
    if package == "ERS" and (oa+sa) >= 256500:
        dataPoints = []
        monthlyPayout = 1134
        dataPoints.append(monthlyPayout)
        for x in range(34):
            monthlyPayout = monthlyPayout*(102/100)
            dataPoints.append(monthlyPayout)
        return dataPoints
    
    return ("Not Enough Money")