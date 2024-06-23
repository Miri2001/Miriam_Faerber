folder = r"C:\Users\miria\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics\Miriam_Faerber\data"
    
# Exercise 1
age = 25
name = "Mario Rossi"
activity = "skating"
job = "engineer"

print(f"Hei, I am {name} \nI am {age} and I love to go {activity} \nI work as an {job}")

#Exercise 2
path = f"{folder}\\01_exe2_data.csv"
with open(path, 'r') as file:
    lines = file.readlines()
for line in lines:
    line= line.strip().split(";")
    analog_reading = line[0].split(":")
    max_voltage = line[1].split(":")
    max_analog = line[2].split(":")
    voltage = float(analog_reading[1])/ float(max_analog[1])* float(max_voltage[1])
    print(voltage)
    
# Exercise 3
string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
print(";".join(string.split(",")))

#Exercise 4
list = [ 1, 2, 3, 4, 5]

for item in list: 
    print(item)

# Exercise 5
list = [ 1, 2, 3, 4, 5]
for item in list:
    print('Number',item)
    
# Exercise 6
list = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]    
for item in range(0, 5):
    print("Number", list[item])
    
# Exercise 7
list1 = [1, 2, 3, 4, 5]
list2 = ["first", "second", "third", "fourth", "fifth"]
for item in range (len(list1)):
    number = list1[item]
    position = list2[item]
    print(f"{position} is {number}")
    
# Exercise 8 

string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
 nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
 pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
 culpa qui officia deserunt mollit anim id est laborum."""
char_count = len(string)
char_count_without_spaces = len(string.replace(" ", ""))
word_count = len(string.split(" "))

print(f"Characters count: {char_count}")
print(f"Characters count without spaces: {char_count_without_spaces}")
print(f"Word count: {word_count}")

# Exercise 9
path = f"{folder}\\01_exe9_data.csv"
with open(path, 'r') as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    if line.startswith("#"):
        continue
    if line:
        print(line)

# Exercise 10
path = f"{folder}\\01_exe9_data.csv"
with open(path, 'r') as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    if line.startswith("#"):
        continue
    if line == "":
        continue
    if float(line[3:])> 1000:
        continue
    print(line)
        

# Exercise 11
path = f"{folder}\\01_exe11_data.csv"
with open(path, 'r') as file:
    lines = file.readlines()
#print(lines)
for line in lines:
    line = line.strip()
    line_split = line.split(";")
    #print(line_split)
    base = line_split[0]
    base = base[5:-2]
    #print(base)
    height = line_split[1]
    height = float(height[7:])*100
    #print(height)
    result = float(base) * float(height) / 2
    #print(result)
    print(f"base * height / 2 = {base} * {height} / 2 = {result}")
    
# Exercise 12.1
who={
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44}
what = {
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
 }
where = {
    44: "to town.",
    11: "in her bed.",
    201: "in the livingroom.",
    23: "up the mountain."
 }

for name, id_ in who.items():
    action = what.get(id_)
    location = where.get(id_)
    print(f"{name} {action} {location}")
  
# Exercise 12.2

who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
 }
what = {
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
 }
where = {
    "runs": "to town.",
    "dreams": "in her bed.",
    "plays": "in the livingroom.",
    "walks": "up the mountain."
 }
for name, id_ in who.items():
    action = what.get(id_)
    location = where.get(action)
    print(f"{name} {action} {location}")   

# Exercise 13
list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

all_lists = list1 + list2 + list3 + list4
print(all_lists)

letter_counter = {}

for item in all_lists:
    count = letter_counter.get(item, 0)
    count += 1
    letter_counter[item] = count
    print(item, "appears", count, "times")
    
# Exercise 14
 #Read the stations.txt file and print out the first 20 lines.
path = f"{folder}\\stations.txt"
with open(path, 'r') as file:
    lines = file.readlines()   
print(lines[:20])
    

# Exercise 15 
print(len(lines))

# Exercise 16
for line in lines[:20]:
    line = line.split(",")
    print(line)
print(len(line))

# Exercise 17
for line in lines[:20]:
    line = line.strip()
    if line.startswith("#"):
        continue
    line_split = line.split(",")
    station_id = line_split[0]
    station_name = line_split[1]
    print(station_id, station_name)
    
# Exercise 18 
#calculate the average height
heights = []
for line in lines:
    line = line.strip()
    if line.startswith("#"):
        continue
    line_split = line.split(",")
    height = float(line_split[-1])
    heights.append(height)
summe = sum(heights)
length = len(heights)
print(summe/length)

# Exercise 19

# Exercise 20

# Exercise 21
n = 10
m = 5
for item in range(n):
    print(m*"*")
    
# Exercise 22
n = 10
m= 1
for item in range(n):
    print(m*"*")
    m +=1
    
# Exercise 23
n = 10
m = 10
for item in range(n):
    print(m*"*")
    m -= 1
    
# Exercise 24
a = 10 
list = []
for item in range(0,a+1):
    if item%2 == 0:
        list.append(item)
print(sum(list))

# Exercise 25
numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
even_numbers = []
for item in numbers: 
    if item%2 ==0:
        even_numbers.append(item)
print(even_numbers)
print(sum(even_numbers))

# # Exercise 26
# # Join the data from the two datasets 01_exe26_dataset1.csv and
# #  01_exe26_dataset2.csv based on the common id and print out the
# #  result
# path = r"C:\Users\miria\OneDrive\OneDrive - Scientific Network South Tyrol\Advanced Geomatics\01_exe26_dataset1.csv"
# with open(path, 'r') as file:
#     lines = file.readlines()
# print(lines)

# path = r"C:\Users\miria\OneDrive\OneDrive - Scientific Network South Tyrol\Advanced Geomatics\01_exe26_dataset2.csv"
# with open(path, 'r') as file:
#     lines_2 = file.readlines()

# dictionary = {}

# for line in lines[1:]:
#     line_split = line.strip().split(',')
#     id_ = line_split[0)
#     values = [float(value) for value in components[1:]]
#     dictionary[id_] = values

# print(dictionary)

# dictionary2 = {}
# for line in lines_2[1:]: 
#     id_2, value = line.split(',')
#     dictionary2[int(id_2)] = value

# print(dictionary2)
    
# merged_dictionary = {}

# for id_, values in dictionary.items():
#     if id_ in dictionary2:
#         merged_dictionary[id_] = values + dictionary2[id_]

# print(merged_dictionary)

    
     
     
     
    

    