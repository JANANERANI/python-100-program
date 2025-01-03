f = 0 #flag
x = int(input("Enter the number to be found out:"))
for i in range(len(numbers)):
  if (x==numbers[i]):
      print(" Successful search, the element is found at position", i)
      f = 1
      break
if(f==0):
  print("Oops! Search unsuccessful")
