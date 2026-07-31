from datetime import datetime


current_time = datetime.now()
# print("Current Time:", current_time)

formatted_time = current_time.strftime("%Y%m%d_%H:%M:%S")
print("Formatted Time:", formatted_time)