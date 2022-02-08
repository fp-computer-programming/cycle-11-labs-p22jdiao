# Author: JD 02/08/2022

my_file = open("alma_mater.txt", "r")
while True:
     line = my_file.readlines()
     line.reverse()
     for x in line:
         print(x)
         print("-")
my_file.close()
