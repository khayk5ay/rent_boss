
import datetime

start_date = datetime.datetime.strptime("2024-01-10", "%Y-%m-%d")
print(start_date)
current_date = datetime.datetime.today()
print("Current Date: ", current_date)
offset = str(int(current_date.day - start_date.day))
print(f" {offset} is offset") 

assert type(offset) == str
