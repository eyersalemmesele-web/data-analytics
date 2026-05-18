# open_and_read.py

f = open("about_me.txt", "r")

# Read one line
print(f.readline(10))

# Read the rest of the line
print(f.readline())

# Read next 4 lines
for i in range(1, 5):
    print(f.readline())

f.close()

# What I learned
# I learned how to use .readline() to read one line at a time.
# I also learned that .readline(10) reads only part of one line.