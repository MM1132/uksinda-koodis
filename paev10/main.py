with open("test.txt") as f:
	raw = f.read().strip()
	lines = [line.strip() for line in raw.split("\n")]

string = lines[0]

def get_shifted_by_one(str, direction):
	new_str = ""
	if direction > 0:
		new_str = str[-1]
		new_str += str[:-1]
	elif direction < 0:
		new_str = str[1:]
		new_str += str[0]
	return new_str

def get_shifted_string(str, amount):
	new_str = str
	
	for _ in range(abs(amount)):
		direction = 1
		if amount < 0:
			direction = -1
		new_str = get_shifted_by_one(new_str, direction)
	return new_str

for line in lines[1:]:
	right = line.split(" ")[1]
	
	if "EEMALDA" in line:
		string = string.replace(right, "")
	elif "LISA" in line:
		string += right
	elif "LIIGUTA PAREMALE" in line:
		right = int(line.split(" ")[2])
		string = get_shifted_string(string, right)
	elif "LIIGUTA VASAKULE" in line:
		right = int(line.split(" ")[2])
		string = get_shifted_string(string, -right)

	# print(line, "->", string)

print(string)
