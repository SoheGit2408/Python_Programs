# import os

# print("Hello world from ...")
# os.system("python --version")

row = int(input("Enter number of rows "))
i,j = 0,0
for i in range(0,row):
  for j in range(0,i + 1):
    print("*",end="")
  print()
  