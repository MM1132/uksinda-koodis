with open("input.txt") as f:
	map = [[char for char in line.strip()] for line in f.readlines()]

# Leiame Lennarti positsiooni
startPos = [0, 0]
for y in range(len(map)):
	for x in range(len(map[y])):
		if map[y][x] == "L":
			map[y][x] = 1
			startPos = [y, x]
			break

def get_sides_from_pos(pos):
	global map

	positions = []
	positions.append([pos[0] - 1, pos[1]])
	positions.append([pos[0] + 1, pos[1]])
	positions.append([pos[0], pos[1] - 1])
	positions.append([pos[0], pos[1] + 1])

	positions = filter(lambda p: p[0] >= 0 and p[0] < len(map) and p[1] >= 0 and p[1] < len(map[0]), positions)
	return positions
distance = 0
def f():
	global map
	queue = [startPos]

	print(f"startPos: {startPos}")

	# Check all 4 sides
	while len(queue) > 0:
		sides = get_sides_from_pos(queue[0])
		for side in sides:
			if map[side[0]][side[1]] == ".":
				map[side[0]][side[1]] = map[queue[0][0]][queue[0][1]] + 1
				queue.append(side)
				# print(f"Queue: {queue}")
			elif map[side[0]][side[1]] == "V":
				return map[queue[0][0]][queue[0][1]]
		queue.pop(0)

exitPos = f()

print(exitPos)
