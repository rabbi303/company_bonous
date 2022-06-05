salary = int(input("Enter salary: " ))
service_year = int(input("Enter year of service: " )) 
bonous= (salary*5/100)
if service_year >= 5:
  print ("Bonous is",bonous)
  print("salary is ", salary+bonous)
else:
  print ("You have no Bonous")
