runs = ["40yd  ", "100m  ", "200m  ", "400m  ", "800m  ", "1km   ", "1500m ", "1mi   ", "2mi   ", "5km   ", "10km  ", "15km  ", "13.1mi", "26.2mi"]
inm = [36.57611031, 100, 200, 400, 800, 1000, 1500, 1609.344498, 3218.688996, 5000, 10000, 15000, 21082.41292, 42164.82584]
b = " "

def hrs(x):
	global hours
	print(b)
	if x == 1:
		hours = int(input("how many hours does it take? "))
	else:
		hours = int(input("how many hours should it take? "))	
	if hours>60 or hours<0:
		hrs()
	hours = hours*3600	

def mins(x):
	global minutes
	print(b)
	if x == 1:
		minutes = int(input("how many minutes does it take? "))
	else:
		minutes = int(input("how many minutes should it take? "))	
	if minutes>60 or minutes<0:
		mins()
	minutes = minutes*60

def secs(x):
	global seconds
	print(b)
	if x == 1:
		seconds = int(input("how many seconds does it take? "))
	else:
		seconds = int(input("how many seconds should it take? "))	
	if seconds>60 or seconds<0:
		secs()

def conversion(x, z):
	if ((x/3600)>=1):
		hh = str(int(x // 3600))
		mm = str(int((x%3600) // 60))
		ss = str((x%3600) % 60)
		if float(hh) < 10:
			hh = "0" + hh
		if float(mm) < 10:
			mm = "0" + mm
		if float(ss) < 10:
			ss = "0" + ss
		print(runs[z] + "--->" + hh + ":" + mm + ":" + ss)
	elif((x/60)>=1):
		mm = str(int(x // 60))
		ss = str(x%60)
		if float(mm) < 10:
			mm = "0" + mm
		if float(ss) < 10:
			ss = "0" + ss
		print(runs[z] + "--->" + "00:" + mm + ":" + ss)
	else:
		x = str(x)
		if float(x) < 10:
			x = "0" + x
		print(runs[z] + "--->" + "00:00:" + x)

def speedmi(x, y):
	indexOf = runs.index("1mi   ")
	multiplier = inm[indexOf] / inm[y-1]
	mitime = x * multiplier
	global mph
	mph = 3600/mitime
	print(str(mph) + " mph")

def speedkm(x, y):
	indexOf = runs.index("1km   ")
	multiplier = inm[indexOf] / inm[y-1]
	mitime = x * multiplier
	global kmph
	kmph = 3600/mitime
	print(str(kmph) + " kmph")


def equivalence(x, y):
	for i in inm:
		indexOf = inm.index(i)
		multiplier = i / inm[y-1]
		multiplied = multiplier*x
		conversion(multiplied, indexOf)

def improver(x, y):
	count = 2
	print(b)
	print("How fast do you need to run " + runs[y-1] + "?")
	hrs(count)
	mins(count)
	secs(count)
	nTime = hours+minutes+seconds
	iTime = x - nTime
	print(b)
	print("Breakdown of improvements by race: ")
	print(b)
	equivalence(iTime, y)
	print(b)
	print("Metric breakdown of improved times: ")
	print(b)
	equivalence(nTime, y)
	print(b)
	speedmi(nTime, y)
	speedkm(nTime, y)

def repeater():
	print(b)
	choice = input("Enter 'yes' to analyze metrics for a different race, anything else will exit the application: ")
	choice = choice.lower()
	if choice == "yes":
		runner()
	else:
		exit()

def runner():
	count = 1
	print(b)
	print("Which race do you need metrics on?")
	print(b)
	for i in runs:
		print(str(runs.index(i)+1) + ". " + i)
	print(b)
	choice = int(input("#: "))
	hrs(count)
	mins(count)
	secs(count)
	time = hours+minutes+seconds
	print(b)
	print("Metric breakdown of race times: ")
	print(b)
	equivalence(time, choice)
	print(b)
	speedmi(time, choice)
	speedkm(time, choice)
	improver(time, choice)
	repeater()


runner()
