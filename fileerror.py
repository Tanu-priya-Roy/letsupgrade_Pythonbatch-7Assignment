#creating file if doesn't exist
try:
	file=open("mywork.txt",'x')
	print("File created")
	file.close()
except FileExistsError:
	print("File already exist")
#opening file in reading mode and trying to write
file=open("mywork.txt",'r')	
try:
	file.write("HELLO WORLD")
except IOError:
	print("File is open in reading mode only")