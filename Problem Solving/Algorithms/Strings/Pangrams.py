line = str(input())
line = line.lower()
line = line.replace(" ", "")
if len(set(line)) == 26:
	print("pangram")
else:
	print("not pangram")