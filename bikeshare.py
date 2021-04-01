import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }     #datasets of the three cities

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
    
    while True:                                     #nfinite loop to repeat the questions if user entered invalid data
       cities = ['chicago','new york','washington'] #list of cities to check user's input 
       city = input('Would you like to see data for chicago , New York , Washington ? \n').lower()  #variable take input from user
       if city == 'all' or city  in cities:         #check that the input is valid 
           
           break
       else:
           
           print('invalid city')
            
    while True:
        
        months=['january','february','march','april','may','june']
    # TO DO: get user input for month (all, january, february, ... , june)
              
        month = input('if you want to filter by month , choose one of months or all ? \n').lower()
              
        if month == 'all'.lower() or month  in months:  #check if input is valid in months or all of them
            
            break
            
        else:
            print('please enter a valid month')

    while True:
        
        days = ['saturday','sunday','monday','tuesday','wednesday','thurusday','friday','all']
        day = input('if you want to filter by the day of the week choose one or all?\n').lower()
        
        if day  in days:
            
            break
        else:
            print('please enter a valid day\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*60)
    
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
    df = pd.read_csv(CITY_DATA[city])                    #read the data from its file to analyze it
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])  #convert [start time ] column to datetime to get information from it
    
    df['month'] =df['Start Time'].dt.month                #inserting month column take the months from start time column
    
    df['day_week']=df['Start Time'].dt.weekday_name       # to get days from the column
    
    df['hour'] = df['Start Time'].dt.hour                #to get hours from the column
    
    if month != 'all'.lower():                           #check if month not all then choose from the months list       
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        month=months.index(month)+1        #convert months from string to its orderd number
        df = df[df['month']==month]
               
    if day != 'all'.lower():
 
        df = df[df['day_week']==day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # TO DO: display the most common month
    
    co_month = df['month'].mode()[0]
    
    print('the most common month is :', co_month)

    # TO DO: display the most common day of week
    
    co_day = df['day_week'].mode()[0]
    
    print('the most common day of the week :', co_day)

    co_hour = df['hour'].mode()[0]
    
    print('The most common hour is : ', co_hour)
    # TO DO: display the most common start hour
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    co_start_station = df['Start Station'].mode()[0]
    
    print('The most common station is : ', co_start_station)
    # TO DO: display most commonly used end station

    co_end_station = df['End Station'].mode()[0]
    print('The most common end station is : ', co_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df['Start Station']+'-'+df['End Station']
    
    co_start_end_station = start_end_station.mode()[0]
    print('most frequent combination of start station and end station trip is :', co_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_time = df['Trip Duration'].sum()
    print('The total travel time is : ' , (t_time/3600) , 'hours')

    # TO DO: display mean travel time
    av_time = df['Trip Duration'].mean()
    print('the mean travel time is : ' ,(av_time/3600),'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    number_of_users = df['User Type'].value_counts()
    
    print('counts of user types is : ' , number_of_users)
    
    # TO DO: Display counts of user types

    # TO DO: Display counts of gender
    
    if 'Gender' in (df.columns):
            
            count_of_gender  = df['Gender'].value_counts()
            print('counts of gender : ' , count_of_gender)
            print('\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        
        earlist_year = df['Birth Year'].min().astype(int)
        
        recent_year = df['Birth Year'].max().astype(int)
        
        co_year = df['Birth Year'].mode()[0].astype(int)
        
        print('The earliest year is : ' , earlist_year)
        
        print('The most recent year is : ' , recent_year)
        
        print('The most common year is : ' , co_year)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
    
def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    raw = input('\nWould you like to diplay raw data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Do you want to show Next 5 raws? yes/no \n')
            if ask.lower() != 'yes':
                break    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
