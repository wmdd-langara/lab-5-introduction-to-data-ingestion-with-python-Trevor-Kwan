#!/usr/bin/env python3
import pandas
import csv

def process_py():
  f = open('prices.csv', 'r')
  header = f.readline().rstrip().split(',')
  total_cost = 0
  num_rows = 0

  for line in f:
     fields = line.rstrip().split(',')
     total_cost += float(fields[14])

     num_rows += 1

  f.close()
  return total_cost/num_rows



def process_csv():
  f = open('prices.csv', 'r')

    # We supply the file object into a reader to parse the csv file
  reader = csv.DictReader(f)

    # initialize some accumulator variables
  total = 0
  count = 0

    # The main loop
  for record in reader:
        # each item in reader is a row in the csv file converted to a python dictionary
      delta = record['PRODUCT_PRICE']
      total += float(delta)
      count += 1

    # remember to close the file object
  f.close()
  return total/count
  

def process_pandas():
  df = pandas.read_csv('prices.csv')


    # We can also perform calculcations on a single column
  delta = df['PRODUCT_PRICE'].mean()

    # We are returning the timedelta
  return delta
  

if __name__ == "__main__":
    print("Average price using pure python: ", end='')    
    print(process_py())
    print("Average price using csv module: ", end='')    
    print(process_csv())
    print("Average price using pandas module: ", end='')    
    print(process_pandas())
