file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

msg = "Hello woorld!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
