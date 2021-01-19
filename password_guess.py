import time

# Assuming that the password is going to only contain numbers [0-9]
# The password can also include the following chars [A, B, C]
password = "12A341B"

# List of possible characters
password_chars = ["A", "B", "C", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Guessing part
guessing_password = ""
tic = time.perf_counter()
while guessing_password != password:
    # Try various combinations of the possible characters
    guessing_password = ""
else:
    toc = time.perf_counter()
    print("Password found: ", guessing_password)
    print("Time taken to guess = "+str(toc-tic)+" seconds.")