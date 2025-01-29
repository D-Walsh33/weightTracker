import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pickle
class Tracker:
    def __init__(self, cur=None, goal=None, fileName='weight.csv', rate=None):
        self.cur = cur
        self.goal = goal
        self.record = pd.read_csv(fileName)
        self.rate = rate
        self.recordFileName = fileName

    def saveRecord(self):
        self.record.to_csv(self.recordFileName)

    def set_goal(self, goal):
        self.goal = goal

    def set_cur(self, cur):
        self.cur = cur
        self.add_record(cur)
    
    def set_rate(self, rate):
        self.rate = rate

    def plot(self):
        """Creates and displays a graph of current progress"""
        df = self.record
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
    
    def get_stats(self):
        """Calculate and display a report to the user"""
        df = self.record
        df['Date'] = pd.to_datetime(df['Date'])
        low = df['Weight'].min()
        numEntries = df['Weight'].count()
        firstWeight = df['Weight'].iloc[0]
        curWeight = df['Weight'].iloc[-1]
        curLost = firstWeight - curWeight
        print(f'Your number of weigh-ins: {numEntries}')
        print(f'Your lowest weight: {low} kg')
        print(f'Your last weigh-in: {curWeight} kg')
        print(f'You have currently lost a total of: {round(curLost, 3)} kgs')
        print(f'Your average weight lost each day: {round(curLost / numEntries, 3)} per day')
        if self.goal:
            print(f'Your goal is to reach {self.goal} kgs.')
        if self.rate:
            print(f'Your goal rate of weight loss is {self.rate} kgs a week.')

    def add_record(self, record):
        today = date.today()
        try:
            weight = float(input("Please enter today's weight in kg:\n"))
        except ValueError:
            print('Invalid weight. Please enter a number')
        data ={'Date': today, 'Weight': weight}
        df2 = pd.DataFrame([data])
        self.record = pd.concat([self.record, df2], ignore_index=True)
    
    def save(self):
        self.saveRecord()
        with open("tracker.pkl", "wb") as f:
            pickle.dump(self, f)
        