import time
import pandas as pd
import numpy as np
# from typing import Any

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    # lower() method here below for making the first char small and make sense with names of cities above

    while True:
        city = input(" Which city you want to select chicago OR new york city OR washington : ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print(" Please select only one of this : chicago OR new york city OR washington ")

        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Which month you want to show it :  ").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if (month != 'all') and (month not in months):
            print("Please select only one of this: january TO june OR all")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Which day of week you want to show it :  ").lower()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if (day not in days) and (day != 'all'):
            print("Please select only one of this: Saturday TO Friday OR all")
            continue
        else:
            break
    print('-' * 40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into data frame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new data frame
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new data frame
        df = df[df['day_of_week'] == day.title()]

    return df


def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while True:
        if view_data == 'no':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: Enter yes or no ").lower()


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_of_month = df['month'].mode()[0]
    print("The most common month is : ", most_common_of_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is : ", most_common_day_of_week)

    # TO DO: display the most common start hour
    # first we wil extract hour from the Start Time column to create an hour column
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour : ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is : ", most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print("The most_commonly_used_end_station is : ", most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Here we can get combination between the start and end station by moding them together

    most_common_trip_between_start_end_station = (df['Start Station'] + " To " + df['End Station']).mode()[0]
    print("The combination between the start and end station is: ", most_common_trip_between_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time in seconds
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # TO DO: display mean travel time in seconds
    average_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(" Counter of user types : ", user_types)

    # TO DO: Display counts of gender
    if city != 'washington' :
        counts_of_gender = df['Gender'].value_counts()
        print(" Counter of gender : ", counts_of_gender)

        # TO DO:
        # Display earliest year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        print("The Earliest year of birth is : {}".format(earliest_year_of_birth))

        # Display most recent
        most_recent_year_of_birth = df['Birth Year'].max()
        print("The most recent year of birth is : {}".format(most_recent_year_of_birth))

        # Display most common year of birth
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print("The  most common year of birth is : {}".format(most_common_year_of_birth))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

    def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            display_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break

    if __name__ == "__main__":
        main()