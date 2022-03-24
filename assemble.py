def main(file_in, file_out):

	try:
		file_in = open(file_in, "r")
		file_out = open(file_out, "w")

	except FileNotFoundError:
		print(f"Error! File {file_in} does not exist!")
		return -1
	
	lines = file_in.read().splitlines()

	to_write = []
	
	for i in range(len(lines)):
		args = lines[i].lower().split(" ")

		if args[0].startswith(";"):
			continue
		if args[0] == "hlt":
			to_write.append("000")
		elif args[0] == "mov":
			if args[1] == "a":
				if args[2] == "b":
					to_write.append("300")
				elif args[2] == "c":
					to_write.append("B00")
				else:
					src = args[2]
					src = hex(int(src, 16))[2:]
					src = src.rjust(2, "0")
				
					to_write.append(f"1{src}")

			if args[1] == "b":
				if args[2] == "a":
					to_write.append("400")
				elif args[2] == "c":
					to_write.append("C00")
				else:
					src = args[2]
					src = hex(int(src, 16))[2:]
					src = src.rjust(2, "0")
				
					to_write.append(f"2{src}")

		elif args[0] == "add":
			to_write.append("500")
		elif args[0] == "sub":
			to_write.append("600")
		elif args[0] == "and":
			to_write.append("700")
		elif args[0] == "or":
			to_write.append("800")
		elif args[0] == "not":
			to_write.append("900")
		elif args[0] == "jmp":
			dest = args[1]
			dest = hex(int(dest, 16))[2:]
			dest = dest.rjust(2, "0")

			to_write.append(f"A{dest}")
		elif args[0] == "out":
			if args[1] == "a":
				to_write.append("D00")
			elif args[1] == "b":
				to_write.append("E00")
			elif args[1] == "c":
				to_write.append("F00")
	
	file_out.write(" ".join(to_write))