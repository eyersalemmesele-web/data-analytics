# open_and_write

# Create and open file in append mode
f = open("about_me.txt", "a")
f.close()

# I learned how to create a file using open() and close it properly.

f = open("about_me.txt", "a")

f.write("\nIf I could have a perfect night out, I would relax, eat good food, and spend time with friends.\n")

f.close()

# I learned how to use .write() to add text into a file.
# I also learned that 'a' mode means append (adds without deleting).

# open_and_write.py

# Open file in append mode
f = open("about_me.txt", "a")

# Add text to the file
f.write("Name: Eyerusalem\n")
f.write("Place of birth: Eritrea\n")
f.write("I live in Dallas, Texas, America.\n")
f.write("I love traveling to Turkey.\n")
f.write("Growing up I had pets.\n")
f.write("My perfect night out would be going to a nice restaurant and coffee shop with friends.\n")

# Close file
f.close()

print("Information added to about_me.txt")