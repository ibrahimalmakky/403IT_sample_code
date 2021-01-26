from datetime import datetime 

current = datetime.now()
print(current.year)
print(current.day)
print(current.strftime("%A %d/%m/%Y %p"))

# Print to a file the current date and time using the following format example: 
# 15:45:45 Tue 26/01/2021 