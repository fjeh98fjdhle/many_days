month_to_days = {"january":31,"februar":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
months_leap_year = {"january":31,"februar":29,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}

def input_usr(timing, year=None, month=None, day=None):
    if timing == "current":
        print("Please enter the current day.")
    elif timing == "goal":
        print("Please enter the target day.")
    if year:
        year = int(input("year:"))
    if month:
        month = input("month(words):")
    if day:
        day = int(input("day:"))
    
    return [year, month, day]

def calculate(current, goal):
    current.append(False)
    goal.append(False)
    #by default the year is not marked as a leap year.
    current.append(0)
    goal.append(0)
    #by default the total number of days is marked as zero:
    
    
    #ausrechnen der totalen Tage
    if goal[0] % 4 == 0:
        goal[3] = True
    if current[0] % 4 == 0:
        current[3] = True
    
    dates = [current, goal]
    
    #days of the years up until now.
    for date in dates:
        for a in range(date[0] -1):
            a += 1
            if a > 1800:
                if a % 4 == 0:
                    date[4] += 366
                else:
                    date[4] += 365
            else:
                date[4] += 365
            

    #current years
    dates = [current, goal]
    for date in dates:
        print(date)
        if date[3] == True:
            month_to_day = months_leap_year
        else:
            month_to_day = month_to_days
            
        for a in month_to_day:            
            date[4] += month_to_day[a]
            if a == date[1]:
                date[4] += date[2]
                break
    

    days_left = goal[4] - current[4] 
    
    return days_left
    
def correction_usr_input(usr_input):
    month = list(usr_input[1])
    fin_month = [""]
    
    count = 0
    for a in month:
        count += 1
        month[count] = month[count].lower()
        fin_month[0] += month_count
    
    right = False
    for month in month_to_days:
        if fin_month[0] == month:
            right = True
            usr_input[1] = fin_month
            
    if right == False:
        print("maybe you made a mistake with the month. Please try again:")
        usr_input = input_usr(year=usr_input[0], month=True, day=usr_input[2])
        correction_usr(usr_input)
        
    return usr_input
            
            
    

def start():
    current = input_usr("current", year=True, month=True, day=True)
    print()
    goal = input_usr("goal", year=True, month=True, day=True)
    difference = calculate(current, goal)
    if difference == 0:
        return "stop joking"
    elif difference < 0:
        return f"your day was {difference * -1} days in the past"
    elif difference > 0:
        return f"your day is {difference} days in the future" 

start()
    
