import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = {"1":"chicago", "2":"new york city", "3":"washington"}

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_selection = input('Please select a city to view data, enter 1 for chicago, 2 for new york, or 3 for washington\n  ').lower()
            if city_selection in cities.keys():
                city = cities[city_selection]
                break
        except KeyboardInterrupt:
                print('NO Input Taken')
        else:
                print('Invalid city choice!!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\n\nTo filter {}\'s data by a particular month, please type the month name as below or type: "all" for not filtering by month: \n-january\n-february\n-march\n-april\n-may\n-june\n-all\n\n:'.format(city.title())).lower()
            if month in months or month == "all":
                break
        except KeyboardInterrupt:
            print('NO Input Taken')
        else:
            print("That's invalid choice, please type a valid month name or all. \nnote: you can only choose from the first 6 months of the year")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\n\nTo filter {}\'s data filterd by {} month(s) by a day, please type the day name as below or type: "all" for not filtering by day: \n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n-all\n\n:'.format(city.title(),month.title())).lower()
            if day in days or day == "all":
                break
        except KeyboardInterrupt:
            print('NO Input Taken')
        else:
            print("That's invalid choice, please type a valid day name or all.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is :", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].value_counts().idxmax()
    print("The most common hour is :", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common starting station is :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common ending station is :", most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common used start station and end station combination is : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total trave time was :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time was :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)
    # TO DO: Display counts of gender
    if ('Gender' not in df.columns) and ('Birth Year' not in df.columns):
        print ('\nGender and Birth Year data is not avaliable for Washington')
    else:
        gender_types = df['Gender'].value_counts(dropna=True)
        print('\nCounts of gender:\n{}'.format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yofb = df['Birth Year'].min()
        most_recent_yofb = df['Birth Year'].max()
        most_common_yofb = df['Birth Year'].mode()[0]
        print('\nthe earliest year of birth= ', earliest_yofb, '\nthe most recent year of birth= ', most_recent_yofb, '\nthe most common year of birth= ', most_common_yofb)
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        counter1=0# counter one
        counter2=5# counter two
        while True:
          ch = input("Would you like to see 5 rows of raw data type yes or no?\n")
          ch=ch.lower() # convert to lower case to capture caps  
          if ch == "yes":
            print(df.iloc[counter1:counter2])
            counter1=counter1+5
            counter2=counter2+5
                       
          else:# if no, break the loop
            break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
