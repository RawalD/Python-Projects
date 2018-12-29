def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds


days_input = int(input("How many days to calculate seconds ? "))
total_seconds = convert_days_to_seconds(days_input)
milliseconds = total_seconds * 1000
print(milliseconds)    
