import requests
import time
import json

time_start = time.time()
#delay = 0
#time.sleep(delay)
req = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json')
time_stop = time.time()
timer = time_stop - time_start

with open('json.txt', 'wb') as f:
    f.write(req.content)

def check_valid_format(filename):
    try:
        with open(filename) as file:
         parse_json = json.load(file) 
         return True
    except ValueError as e:        
        return False

begin = time.time()
x = 10
y = 5
z = 1

def multi_check_valid_format(filename, file2, x, y, z):
    while z<=x:
        now = time.time()
        loop_time = now - begin
        print(check_valid_format(filename))
        print(loop_time)
        file2.write(str(check_valid_format(filename)))
        file2.write(' ')
        file2.write(str(loop_time))
        file2.write('\n')
        z +=1
        time.sleep(y)

file = open("log.txt", "w")

print(timer)
print(req.status_code)
print(req.headers)
#print(req.text)
print(check_valid_format('json.txt'))
print('\n')
#print(multi_check_valid_format('json.txt', x, y, z))

file.write(str(time.localtime()))
file.write('\n')
file.write(str(timer))
file.write('\n')
file.write(str(req.status_code))
file.write('\n')
file.write(str(req.headers))
file.write('\n')
file.write(str(check_valid_format('json.txt')))
file.write('\n')
file.write(str(multi_check_valid_format('json.txt', file, x, y, z)))
file.close()




