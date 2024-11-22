import calendar

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def working_days(month,year):
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
        "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
        "November": 11, "December": 12
    }
    month_num = month_map[month]
    num_days = calendar.monthrange(year,month_num)[1]
    
    prime_day_count = 0 
    for day in range(1,num_days+1):
        if is_prime(day):
            prime_day_count+=1
    return prime_day_count
    
month,year=input().split()
year = int(year)

print(working_days(month,year))
