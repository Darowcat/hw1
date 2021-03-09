import csv
#=======================================

cwb_filename = '107061202.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

data = list(filter(lambda item: item['TEMP'] != '-99.000' and item['TEMP'] != '-999.000', data))

rows, cols = (5, 2) 
arr = []
max_arr = []
ans = [[0 for i in range(cols)] for j in range(rows)] 
#1
arr = list(filter(lambda item: item['station_id'] == 'C0A880', data))
if not arr : 
   ans[0].extend(['C0A880', 'NONE'])
else : 
   max_arr = max(arr, key = lambda item: item['TEMP'])
   ans[0].extend([max_arr['station_id'], max_arr['TEMP']])

ans[0] = ans[0][2:4]
#2
arr = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
if not arr : 
   ans[1].extend(['C0F9A0', 'NONE'])
else : 
   max_arr = max(arr, key = lambda item: item['TEMP'])
   ans[1].extend([max_arr['station_id'], max_arr['TEMP']])

ans[1] = ans[1][2:4]
#3
arr = list(filter(lambda item: item['station_id'] == 'C0G640', data))

if not arr : 
   ans[2].extend(['C0G640', 'NONE'])
else : 
   max_arr = max(arr, key = lambda item: item['TEMP'])
   ans[2].extend([max_arr['station_id'], max_arr['TEMP']])
   ans[2] = ans[2][2:4]
#4
arr = list(filter(lambda item: item['station_id'] == 'C0R190', data))
if not arr : 
   ans[3].extend(['C0R190', 'NONE'])
else : 
   max_arr = max(arr, key = lambda item: item['TEMP'])
   ans[3].extend([max_arr['station_id'], max_arr['TEMP']])

ans[3] = ans[3][2:4]
#5
arr = list(filter(lambda item: item['station_id'] == 'C0X260', data))
if not arr : 
   ans[4].extend(['C0A880', 'NONE'])
else : 
   max_arr = max(arr, key = lambda item: item['TEMP'])
   ans[4].extend([max_arr['station_id'], max_arr['TEMP']])

ans[4] = ans[4][2:4]
#ans[0].extend([max(list(filter(lambda item: item['station_id'] == 'C0A880', data)), key = lambda item: item['TEMP'])['station_id'], max(list(filter(lambda item: item['station_id'] == 'C0A880', data)), key = lambda item: item['TEMP'])['TEMP']])
#ans[0] = ans[0][2:4]
#ans[1].extend([max(list(filter(lambda item: item['station_id'] == 'C0F9A0', data)), key = lambda item: item['TEMP'])['station_id'], max(list(filter(lambda item: item['station_id'] == 'C0F9A0', data)), key = lambda item: item['TEMP'])['TEMP']])
#ans[1] = ans[1][2:4]
#ans[2].extend([max(list(filter(lambda item: item['station_id'] == 'C0G640', data)), key = lambda item: item['TEMP'])['station_id'], max(list(filter(lambda item: item['station_id'] == 'C0G640', data)), key = lambda item: item['TEMP'])['TEMP']])
#ans[2] = ans[2][2:4]
#ans[3].extend([max(list(filter(lambda item: item['station_id'] == 'C0R190', data)), key = lambda item: item['TEMP'])['station_id'], max(list(filter(lambda item: item['station_id'] == 'C0R190', data)), key = lambda item: item['TEMP'])['TEMP']])
#ans[3] = ans[3][2:4]
#ans[4].extend([max(list(filter(lambda item: item['station_id'] == 'C0X260', data)), key = lambda item: item['TEMP'])['station_id'], max(list(filter(lambda item: item['station_id'] == 'C0X260', data)), key = lambda item: item['TEMP'])['TEMP']])
#ans[4] = ans[4][2:4]

print(ans)