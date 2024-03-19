import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

if (hour < 12):
  print("good morning boss")
elif (hour > 12 and hour < 5):
    print("good afternoon boss")
else:
    print("good evening boss")