import sys

# redirecting stdout to file
print("coming through stdout")
# stdout is saved
save_stdout = sys.stdout
fh = open('test.txt', 'w')
sys.stdout = fh
print('this line goes to test.txt')
# return to normal
sys.stdout = save_stdout
fh.close()


# redirecting stderr to file
save_stderr = sys.stderr
fh = open('errors.txt', 'w')
sys.stderr = fh
x = 10/0
# return to normal
sys.stderr = save_stderr
fh.close()


# It is possible to write into the error stream directly, i.e. without changing the general output behaviour.
# This can be achieved by appending >> sys.stderr to a print statement.

save_stderr = sys.stderr
fh = open("errors.txt", "w")
sys.stderr = fh
print(sys.stderr, 'printing to error.txt')
# return to normal
sys.stderr = save_stdout
fh.close()
