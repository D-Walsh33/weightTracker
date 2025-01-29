from tracker import Tracker
import pickle

def track_weight():
    """Tracks weight over time and provides a visualization of your progress."""
    try:
        with open(tracker_file_path, 'x') as file:
            tracker = Tracker()
    except FileExistsError:
            with open(tracker_file_path, "rb") as f:
                tracker = pickle.load(f)

    greeting()
    while True:
        response = input('Please enter a command:\n').upper()
        match response:
            case 'L':
                print('\nlogging!\n')
                tracker.add_record()

            case 'D':
                print('\nPrinting!\n')
                print(tracker.record)
            
            case 'R':
                print('Reporting!')
                tracker.get_stats()
            
            case 'SG':
                print('Setting Goal!')
                goal = float(input("Enter your goal weight in KG's \n"))
                tracker.set_goal(goal)
            
            case 'SR':
                print('Setting Rate!')
                rate = float(input("Enter the number of KG's you would like to lose a week: \n"))
                tracker.set_rate(rate)

            case 'P':
                print('\nGraphing!\n')
                tracker.plot()

            case 'Q':
                print('\nQuiting!\n')
                tracker.save()
                break

            case 'H':
                command()

            case _:
                print('\nInvalid Command\n')

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
    weight_file_path = "weight.csv"
    tracker_file_path = "tracker.pkl"
    try:
        with open(weight_file_path, 'x') as file:
            file.write("Date,Weight")
        track_weight()
    except FileExistsError:
        track_weight()