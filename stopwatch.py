import time
wait = time.sleep

def stopwatch():
	second = 0
	minute = 0
	hour = 0
	day = 0
	week = 0
	month = 0
	for i in range((-2**23),(2**23-1)):
		wait(1)
		second = second + 1
		print(month,"mo :",week,"w :",day,"d :",hour,"h :",minute,"m :",second,"s")
		if second >= 59:
			minute = minute + 1
			second = -1
		if minute >= 59.9833333:
			hour = hour + 1
			minute = 0
			second = -1
		if hour >= 23.9997222:
			day = day + 1
			hour = 0
			minute = 0
			second = -1
		if day >= 6.99998843:
			week = week + 1
			day = 0
			hour = 0
			minute = 0
			second = -1
		if week >= 3.999998342857:
			month = month + 1
			week = 0
			day = 0
			hour = 0
			minute = 0
			second = -1
stopwatch()

# The maximum amount of days the stopwatch can last before reaching
# its limit is 194 days, 4 hours, 20 minutes, and 15 seconds.