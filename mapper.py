import sys

def mapper():
	for line in sys.stdin:
		line = line.strip('\n')
		data = line.split(';')
		id = data[2]
		time = data[3]
		print(id + "\t" + time)

if __name__ == '__main__':
	mapper()