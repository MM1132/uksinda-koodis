class City:
	def __init__(self, name):
		self.name = name
		self.connections = {}
		self.visited = False
		self.depth = None
	
	def addConnection(self, otherCity):
		self.connections[otherCity.name] = otherCity
	
	def __str__(self):
		outputString = f"{self.name} is connected to: "
		for c in self.connections:
			outputString += f"{self.connections[c].name}, "
		outputString += f"Depth: {self.depth}"
		return outputString

with open("test.txt") as f:
	lines = [line.strip() for line in f.readlines()]

cities = {}

for line in lines:
	city = line.split(": ")[0]
	otherCities = line.split(": ")[1].split(", ")

	if city not in cities:
		cities[city] = City(city)
	for otherCity in otherCities:
		if otherCity not in cities:
			# print(f"Other city: {otherCity}")
			cities[otherCity] = City(otherCity)
		cities[otherCity].addConnection(cities[city])
		cities[city].addConnection(cities[otherCity])

queue = [cities["New York"]]
queue[0].depth = 1
while len(queue) > 0:
	queue[0].visited = True
	for city in queue[0].connections:
		if cities[city].visited == False:
			if cities[city] not in queue:
				cities[city].depth = queue[0].depth + 1
				queue.append(cities[city])
	queue.pop(0)

# for city in cities:
# 	print(cities[city])

for city in cities:
	if city == "Tartu":
		print(cities[city].depth - 2)
