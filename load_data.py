#!/usr/bin/env python3
import pandas
import csv
import json


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
  reader = csv.DictReader(f)

  # initialize some accumulator variables
  total = 0
  count = 0

  for record in reader:
        # each item in reader is a row in the csv file converted to a python dictionary
      delta = record['PRODUCT_PRICE']
      total += float(delta)
      count += 1

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



def process_csv_dict():
  f = open('prices.csv', 'r')
  reader = csv.DictReader(f)

  keys = []
  values = []
  count = []
  avg_cost = []

  #if not in dictionary then initiate key and value = 0 for it and a count(er)
  for record in reader:
    if record['ITEM_CATEGORY_NAME'] not in keys:
       keys.append(record['ITEM_CATEGORY_NAME'])
       values.append(float(0))
       count.append(float(0))

  #go back to the start of the csv file; first row 
  f.seek(0)

  #add up all the prices 
  for record in reader:
     price = record['PRODUCT_PRICE']
     category = record['ITEM_CATEGORY_NAME']

     for i in range (len(keys)):
       if keys[i] == str(category):
        values[i] += float(price)
        count[i] += float(1)
  
  #avg cost from total divided by count 
  for i in range (len(values)):
    if count[i] == 0:
      avg_cost.append(185)
  
    else:
      avg_cost.append(values[i]/count[i])


  #combine together to form a dictionary 
  res = {keys[i]: avg_cost[i] for i in range (len(avg_cost))}
  #a_dict = {key: res[key] for key in res if key != "^invalid"}
  

  f.close()
  return res

print(process_csv_dict())




'''def process_pandas_groupby():
  
  datas = process_csv_dict()
  d = {'ITEM_CATEGORY_NAME': datas.keys(), 'PRODUCT_PRICE': datas.values()}
  df = pandas.DataFrame(data = d)
  df

  df.groupby(['ITEM_CATEGORY_NAME'])
  return df'''


def process_pandas_groupby():
  df = pandas.read_csv('prices.csv')
    # We can also perform calculcations on a single column
  delta = df[['ITEM_CATEGORY_NAME', 'PRODUCT_PRICE']]

  avg = delta.groupby(['ITEM_CATEGORY_NAME']).mean()
    # We are returning the timedelta
  return avg

print(process_pandas_groupby())