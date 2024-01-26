import csv
import calendar
import os

def findDay(date):
    year, month, day = (int(i) for i in date.split('-'))    
    dayNumber = calendar.weekday(year, month, day)
    # Modify days list to start with Sunday as 0
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]    
    return days[dayNumber+1]

def date_translate(date):
    year, month, day = (int(i) for i in date.split('-')) 
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return year, months[month-1], day

def write_to_csv(row, date):
    year, month, day = date_translate(date)
    # Create directories if they don't exist
    directory = f'app/data/{year}/{month}/'
    os.makedirs(directory, exist_ok=True)

    # Open the CSV file for writing
    with open(f'{directory}{day}.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        
def read_from_csv(date):
    year, month, day = date_translate(date)
    with open(f'app/data/{year}/{month}/{day}.csv', mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data