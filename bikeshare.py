import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities = ["Chicago", "New York", "Washington"]
    city = input("Which city do you want to see data for? Chicago, New York City, or Washington? ").lower()
    while True:
        if city in ["chicago", "new york city", "washington"]:
            print("Ok, we will look at data for {}.".format(city).title())
            break
        if city not in ["chicago", "new york city", "washington"]:
            print("Please double check the city you entered and ensure it matches one of the three choices. Try again.")
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month do you want to see data for? All, January, February, March, April, May, June: ").lower()
    while True:
        if month in ["all", "january", "february", "march", "april", "may", "june"]:
            print("We will look at data for {}.".format(month).title())
            break
        if month not in ["all", "january", "february", "march", "april", "may", "june"]:
            print("Please double check the month you entered and ensure it matches one of the choices. Try again.")
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Which day do you want to see data for? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: "))
    while True:
        if day in ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            print("We will look at data for {}.".format(day))
            break
        if day not in ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            print("Please double check the day you entered and ensure it matches one of the choices. Try again.")
            break

    print('-'*40)
    return city, month, day


    import pandas as pd



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
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    start_hour = df['start_hour'].mode()[0]
    print('Most Common Start Hour:', start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip

    combo = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start stations and end stations is: \n', combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('The total travel time (in seconds) is:', trip_duration)
    print('The total travel time (in minutes) is:', trip_duration / 60)

    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print('The mean travel time is:', trip_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts =  df['User Type'].value_counts()
    print('The user types are: \n', user_type_counts)

    # TO DO: Display counts of gender
    gender_counts =  df['Gender'].value_counts()
    print('The gender counts are: \n', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = int(df['Birth Year'].min())
    print('The earliest birth year is:', earliest_birth_year)

    latest_birth_year = int(df['Birth Year'].max())
    print('The most recent birth year is:', latest_birth_year)

    common_year = int(df['Birth Year'].mode()[0])
    print('The most common birth year is:', common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            response = input("Please enter yes if you like to see 5 rows of data. Enter no if not. ").lower()
            if response == "yes":
                 raw = np.array([1, 2, 3, 4, 6]).reshape(6, 1)
                 print(raw)
            else:
                     print("Finished.")
                     break

            response = input("Please enter yes if you like to see 5 additional rows of data. Enter no if not. ").lower()
            if response == "yes":
                raw = np.array([1, 2, 3, 4, 6]).reshape(6,1) + 5
                print(raw)
            else:
                print("Finished. Please exit.")
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
