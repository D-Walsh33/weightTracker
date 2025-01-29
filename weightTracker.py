import pandas as pd
import matplotlib.pyplot as plt
# importing date module
from datetime import date
from matplotlib.dates import DateFormatter

def track_weight():
    """Tracks weight over time and provides a visualization of your progress."""
    greeting()
    df = load(file_path)
    while True:
        response = input('Please enter a command:\n').upper()
        match response:
            case 'L':
                print('\nlogging!\n')
                df = log(df)

            case 'D':
                print('\nPrinting!\n')
                display(df)
            
            case 'R':
                print('Reporting!')
                report(df)

            case 'G':
                print('\nGraphing!\n')
                graph(df)

            case 'Q':
                print('\nQuiting!\n')
                quit(df)
                break

            case 'H':
                command()

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

def report(df):
    """Calculate and display a report to the user"""
    df['Date'] = pd.to_datetime(df['Date'])
    low = df['Weight'].min()
    numEntries = df['Weight'].count()
    firstWeight = df['Weight'].iloc[0]
    curWeight = df['Weight'].iloc[-1]
    curLost = firstWeight - curWeight
    print(f'Your number of weigh-ins: {numEntries}')
    print(f'Your lowest weight: {low} kg')
    print(f'Your last weigh-in: {curWeight} kg')
    print(f'You have currently lost a total of: {curLost} kgs')
    print(f'Your average weight lost each day: {curLost / numEntries} per day')


def graph(df):
    """Creates and displays a graph of current progress"""
    df['Date'] = pd.to_datetime(df['Date'])
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Weight'])
    ax.set_xticks(df['Date'])
    myFmt = DateFormatter('%m - %d')
    ax.xaxis.set_major_formatter(myFmt)
    #this tilts the dates
    fig.autofmt_xdate()
    ax.set_title('2025 Weight Loss!')
    plt.show()


def quit(df):
    """Saves data to CSV file and quits application"""
    df.to_csv(file_path, index=False )

def load(fileName):
    """Loads previous data from local CSV file"""
    return pd.read_csv(fileName)

def greeting():
    """Greets user and displays available commands."""
    print('Welcome to Weight Tracker 2025!\n')
    print('Commands: L-D-G-Q-R H For details')

def command():
    """Collects users command"""
    print('Commands:')
    print('L: Log a new Weight')
    print('D: Display all records')
    print('G: Graph progress')
    print('R: Report of progress')
    print('Q: Quit program\n')

if __name__ == '__main__':
    file_path = "weight.csv"
try:
    with open(file_path, 'x') as file:
        file.write("Date,Weight")
    track_weight()
except FileExistsError:
    track_weight()