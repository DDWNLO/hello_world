import pandas as pd 

#Set vars
name='Dennis'
number=10

#Cast the int to string
str_number=str(number)

#Concat to 1 string
con_string=name+'_'+str_number

#import csv to dataframe
airports_df=pd.read_csv('airports.csv')

df_read= airports_df["city"]


#commentaar bij print
#print(con_string)

print(df_read)
