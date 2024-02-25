from random import *
from os import makedirs, path
from string import *

# create testcases folder if not exist
if not path.exists("./testcases"):
    makedirs("./testcases")

# generate testcase
testcase_number_start = 5
testcase_number_end = 6
for testcase_number in range(testcase_number_start, testcase_number_end + 1):
    testcase_path = path.join("./testcases", str(testcase_number) + ".in")
    with open(testcase_path, "w") as file:
        # write file here for each testcases
        a = randint(0, 1000)
        b = randint(0, 1000)
        c = randint(0, 1000)
        d = randint(0, 1000)
        file.write(str(a) + ' ' + str(b) + "\n")
        file.write(str(a) + ' ' + str(d) + "\n")
