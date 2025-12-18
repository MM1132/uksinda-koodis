import re
# import time
from datetime import datetime, time, timedelta

# import sys
# sys.setrecursionlimit(10000)

class Trip:
	hourPattern = re.compile(r'(\d+)h')
	minutePattern = re.compile(r'(\d+)m')
	
	# Init trip just from the line itself
	def __init__(self, line):
		self.cityFrom = line.split(" →")[0]
		self.cityTo = line.split("→ ")[1].split(" --")[0]

		# Get the duration of the trip
		h = int(Trip.hourPattern.search(line).groups()[0])
		m = int(Trip.minutePattern.search(line).groups()[0])
		self.duration = timedelta(hours=h, minutes=m)

		# Departures
		self.departures = []
		departures = line.split("Väljumised: ")[1].split(" ")
		for d in departures:
			dh = int(d.split(":")[0])
			dm = int(d.split(":")[1])
			departureTime = datetime(2025, 12, 1, dh, dm)
			self.departures.append(departureTime)
	
	def __str__(self):
		outputString = f"{self.cityFrom} -> {self.cityTo}, {self.duration} "

		outputString += "Departures: "
		for d in self.departures:
			outputString += f"{d} "

		return outputString

class City:
	def __init__(self, name):
		self.name = name
		self.trips = []
		self.visited = False
	
	def addTrip(self, trip):
		self.trips.append(trip)

	def __str__(self):
		outputString = f"City: {self.name}; "

		outputString += "From here you can go to: "
		outputString += " ".join([t.cityTo for t in self.trips])

		return outputString

with open("input.txt") as f:
	lines = f.readlines()

cities = {
	"Tallinn": City("Tallinn")
}
for line in lines:
	trip = Trip(line)
	
	if trip.cityFrom not in cities:
		cities[trip.cityFrom] = City(trip.cityFrom)
	cities[trip.cityFrom].addTrip(trip)

# From here we can just add the recursion

print(f"City count: {len(cities)}")

fastestCombination = [None, 1440]

def f(timePassed = datetime(2025, 12, 1, 0, 0), alreadyVisitedCities = ["Tartu"]):
	global fastestCombination

	# When more than 24 hours have passed
	elapsedMinutes = int((timePassed - datetime(2025, 12, 1, 0, 0)).total_seconds() // 60)

	if elapsedMinutes >= fastestCombination[1]:
		return False
	
	currentCity = alreadyVisitedCities[-1]
	
	if currentCity == "Tallinn":
		fastestCombination = [alreadyVisitedCities, elapsedMinutes]
		
		print(f"Found another one, with length of {len(fastestCombination[0])}")
		print(" ".join(fastestCombination[0]), fastestCombination[1])
		return [alreadyVisitedCities, elapsedMinutes]
	
	# cities[currentCity].visited = True

	# Try to go to another city
	# All the possible trips from our current city
	for trip in cities[currentCity].trips:
		# if cities[trip.cityTo].visited:
		# 	continue

		# If we have not already visited the city
		if trip.cityTo in alreadyVisitedCities:
			continue
		# If that trip has a departure where we would have to wait less than 2 hours
		for departure in trip.departures:
			if departure < timePassed:
				continue
			minutesAway = (departure - timePassed).seconds / 60
			# if (minutesAway < 60):
			newTime = timePassed + trip.duration + timedelta(minutes=minutesAway)
			f(newTime, [*alreadyVisitedCities, trip.cityTo])
			break

f()
print(" ".join(fastestCombination[0]), fastestCombination[1])

# 196597
# 854797
# 1999174
# Tartu Armisvesi Sinalepa Asundus Vabriku Replot Tiri Liinankivaara Vahtra Tallinn 1169
