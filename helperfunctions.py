import math

def get_std_deviation(daily_returns : list) : 
    """
    return ths standard deviation of the array
    """

    # np.std(daily_returns)

    # the standard deviation of an array can also be calculated 
    # with the help of the above formula

    # formula of std deviation : σ = √(∑(x− mean)**2 /n)

    sum = 0 
    for x in daily_returns : sum += x

    meanvalue = sum/len(daily_returns)
    
    denominator = len(daily_returns)
    numerator = 0 
    for x in daily_returns : 
        numerator += (x-meanvalue)**2
    
    squaredsigma = numerator/denominator

    std_deviation = math.sqrt(squaredsigma)

    return  std_deviation

def annualizedVolatility(dailyvolitality : float , samplelength : int) : 
    squarootLen = math.sqrt(samplelength)
    return dailyvolitality*squarootLen