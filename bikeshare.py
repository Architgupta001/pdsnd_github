import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': '.\data\chicago.csv',
              'new york city': '.\data\\new_york_city.csv',
              'washington': '.\data\washington.csv' }

def common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    popular_month=df['month'].mode()[0]
    print('Most Popular Start Month:',popular_month)
def common_day(df):
    df['day'] = df['Start Time'].dt.day_name()
    popular_day=df['day'].mode()[0]
    print('Most Popular Day:',popular_day)
def common_start_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour:',popular_hour)
def filter_day():
    days_option=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    while True: 
        day =input('\nWhich day ? Choose sunday, monday, tuesday, wednesday, thursday, friday or saturday\n') 
        day=day.lower()
        if(day in days_option):
            break
    return day
def filter_month():
    month_option=['january','february','march','april','may','june','july','august','september','october','november','december']
    while True:
        month =input('\nWhich month ? Choose january, february, march, april, may, june, july, august, september, october, november or december\n') 
        month=month.lower()
        if(month in month_option):
            break
    return month

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df
def get_filters():
    print('Welcome,Explore some US Bikeshare data!')
    city_option=['chicago','new york city','washington']
    while True:
        city =input('\n choose one of the following cities (Chicago, New York city, Washington)\n')
        city=city.lower()
        if(city in city_option):
            break
    while True:
        filter_option=[1,2,3,4]
        filter =input('\n Would you like to filter using \n1:month\n2:day\n3:both\n4:not at all\n Type 1, 2, 3, or 4\n')
        filter=int(filter)
        if(filter in filter_option):
            break
    if(filter==1):
        month=filter_month()
        day='all'
    elif(filter==2):
        day=filter_day()
        month='all'
    elif(filter==3):
        month=filter_month()
        day=filter_day()
    elif(filter==4):
        day='all'
        month='all'
    
    print('-'*40)
    return city, month, day

def time_stats(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if(month=='all' and day=='all'):
        common_month(df)
        common_day(df)
        common_start_hour(df)
    elif(month!='all' and day=='all'):
        common_day(df)
        common_start_hour(df)
    elif(month=='all' and day!='all'):
        common_start_hour(df)
        common_month(df)
    elif(month!='all'and day!='all'):
        common_start_hour(df)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('Most Popular most frequent combination of start station and end station: ',popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        load_data(city, month, day)
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        flag=1
        start=0
        end=5
        while(flag ==1):
            flag=int(input('\nWould you like to view individual trip data? \nType 1 or 2 \n1:True\n2:False\n'))
            while((flag != 1) and (flag!=2)):
                flag=int(input('\nPlease enter available input: '))
            print(df.iloc[start:end])
            start+=5
            end+=5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart = restart.lower()
        while((restart != 'yes') and (restart !='no')):
            restart=input('\nPlease enter available input: ')
        if restart == 'no':
            break
        elif restart =='yes':
            continue

def user_stats(df,city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print('User Type:\n',user_types)
    if city=='new york city' or city=='chicago':
          gender_types = df['Gender'].value_counts()
          print('Gender Type:\n',gender_types)
          earliest_year_birth = int(df['Birth Year'].min())
          print('Earliest Year Birth: ',earliest_year_birth)
          most_recent_year_birth =int(df['Birth Year'].max())
          print('Most Recent Year Birth: ',most_recent_year_birth)
          most_common_year_birth = int(df['Birth Year'].mode()[0])
          print('Most common Year Birth: ',most_common_year_birth)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


if __name__ == "__main__":
	main()