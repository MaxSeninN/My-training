from sys import argv

script_name, hour_work, rate_per_hour, prize = argv
def my_fnc(hour_work, rate_per_hour, prize):
    hour_work = int(hour_work)
    rate_per_hour = int(rate_per_hour)
    prize = int(prize)
    return hour_work * rate_per_hour + prize

print(my_fnc(hour_work, rate_per_hour, prize))