import sys

def read_file(file_in_name, index_to_remove, number_of_header_lines):
	file = open(file_in_name)
	lines = file.readlines()
	list_of_lines = []
	for line in lines[number_of_header_lines:]:
		lis = line.split()
		lis.pop(index_to_remove)
		new_line = " ".join(lis)
		list_of_lines.append(new_line)
	file.close()
	return list_of_lines

def write_file(file_out_name, list_of_lines):
	file = open(file_out_name, "w")
	for line in list_of_lines:
		file.write(line + '\n')
	file.close()

def main():
	file_in_name = input("Old file name: ")
	file_out_name = input ("New file name: ")
	index_to_remove = int(input("Column to be removed: ")) - 1
	number_of_header_lines = int(input("Number of header lines to ignore: "))

	list_of_lines = read_file(file_in_name, index_to_remove, number_of_header_lines)
	write_file(file_out_name, list_of_lines)

main()

# TO-DO
# Add ability to enter multiple columns
# Add ability to choose what the data is seperated by (commas, spaces, anything)
