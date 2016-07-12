import sys

def reduce():
	subtotal = 0
	previous_id = None
	for line in sys.stdin:
		line = line.strip('\n')
		id = line.split('\t')[0]
		time = int(line.split('\t')[1])
		if previous_id == None:
			previous_id = id		
		if previous_id == id:
			subtotal += time
		if previous_id != id:	
			print previous_id + ', ' + str(subtotal)
			previous_id = id
			subtotal = 0
			subtotal += time
	print previous_id + ', ' + str(subtotal)

if __name__ == '__main__':
	reduce()