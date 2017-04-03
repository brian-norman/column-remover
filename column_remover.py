import sys

def read_file(file_in_name, index_to_remove, number_of_header_lines, seperated_by):
	file = open(file_in_name)
	lines = file.readlines()
	list_of_lines = []

	for line in lines[number_of_header_lines:]:
		lis = line.split(seperated_by)
		for index in reversed(index_to_remove):
			lis.pop(index)
		new_line = " ".join(lis)
		list_of_lines.append(new_line)
	file.close()
	return list_of_lines

def write_file(file_out_name, list_of_lines):
	file = open(file_out_name, "w")
	for line in list_of_lines:
		file.write(line)
	file.close()

def main():
	file_in_name = input("Old file name: ")
	file_out_name = input ("New file name: ")
	number_of_header_lines = int(input("Number of header lines to ignore: "))
	seperated_by = input("Data seperated by (if space, enter space): ")
	
	index_to_remove = input("Column to be removed (if multiple, seperate by space, ascending order): ")
	if len(index_to_remove) > 1:
		index_to_remove = index_to_remove.split()
		for i, index in enumerate(index_to_remove):
			index_to_remove[i] = int(index) - 1
	elif len(index_to_remove) == 1:
		index_to_remove = [int(index_to_remove) - 1]

	list_of_lines = read_file(file_in_name, index_to_remove, number_of_header_lines, seperated_by)
	write_file(file_out_name, list_of_lines)

if __name__ == "__main__":
	main()

# TO-DO
# Add ability to include header lines in output file or not
