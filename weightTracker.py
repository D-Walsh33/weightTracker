import pandas as pd
import matplotlib as plt
# importing date module
from datetime import date

def track_weight():
    """Tracks weight over time and provides a visualization of your progress."""
    greeting()
    df = load(file_path)
    while True:
        response = command().upper()
        match response:
            case 'L':
                print('\nlogging!\n')
                df = log(df)

            case 'D':
                print('\nPrinting!\n')
                display(df)
            case 'G':
                print('\nGraphing!\n')
                graph()

            case 'Q':
                print('\nQuiting!\n')
                quit(df)
                break

            case _:
                print('\nInvalid Command\n')


def log(df):
    """Logs a new weight"""
    today = date.today()
    try:
        weight = float(input("Please enter today's weight in kg:\n"))
    except ValueError:
        print('Invalid weight. Please enter a number')
    data ={'Date': today, 'Weight': weight}
    df2 = pd.DataFrame([data])
    return pd.concat([df, df2], ignore_index=True)

def display(df):
    """Prints all logs to date"""
    print(df)

def graph():
    """Creates and displays a graph of current progress"""
    pass

def quit(df):
    """Saves data to CSV file and quits application"""
    df.to_csv(file_path, index='Date')

def load(fileName):
    """Loads previous data from local CSV file"""
    return pd.read_csv(fileName)

def greeting():
    """Greets user and displays available commands."""
    print('Welcome to Weight Tracker 2025!\n')

def command():
    """Collects users command"""
    print('Commands:')
    print('L: Log a new Weight')
    print('D: Display all records')
    print('G: Graph progress')
    print('Q: Quit program\n')
    return input('Please enter a command:\n')

if __name__ == '__main__':
    file_path = "weight.csv"
try:
    with open(file_path, 'x') as file:
        file.write("Date,Weight")
    track_weight()
except FileExistsError:
    track_weight()