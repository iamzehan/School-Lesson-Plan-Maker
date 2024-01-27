import os
import csv
import calendar
from datetime import datetime

def convert_to_datetime(date_string):
    date_format = "%Y-%b-%d"
    datetime_object = datetime.strptime(date_string, date_format)
    return datetime_object.date()

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

def write_to_csv(row, date, _class, section):
    year, month, day = date_translate(date)
    # Create directories if they don't exist
    directory = f'app/data/{year}/{month}/Class - {_class}/Section - {section}'
    os.makedirs(directory, exist_ok=True)

    # Open the CSV file for writing
    with open(f'{directory}/{day}.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        
def read_from_csv(date, _class, section):
    year, month, day = date_translate(date)
    with open(f'app/data/{year}/{month}/Class - {_class}/Section - {section}/{day}.csv', mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def add_rows(rows):
    my_table = f"""<tr align="center">
                        <th>Subject</th>
                        <th>Period</th>
                        <th>C.W.</th>
                        <th>H.W.</th>
                    </tr>
                    {rows}"""
    return my_table


def show_table(data, date):
    rows = []
    date = f"""{date} ({findDay(str(date))})"""
    for row in data:
        if len(row)>1:
            rows.append(f"""<tr align="center">
                        <td>{str(row[1])}</td>
                        <td>{str(row[2])}</td>
                        <td>{row[3]}</td>
                        <td>{row[4]}</td>
                    </tr>
                """)
        if len(row)==1:
            rows.append(f"""<tr align="center">
                    <td colspan=4>{"".join(row)}</td>
                </tr>""")
    rows = """""".join(rows)
    return f"""<table align="middle" style="width:100%; border:1px solid black;">
                <tr align="center" border:1px solid black;><th style='background-color:aqua'>Date & Day</th><td colspan=3>{date}</td></tr>
                    {add_rows(rows)}</table>"""