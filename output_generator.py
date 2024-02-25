from os import path
from subprocess import run

# compile solution
run(["g++", "solution.cpp"])

# create output file by solution
testcase_count = 20
for testcase_number in range(1, testcase_count + 1):
    input_path = path.join("./testcases", str(testcase_number) + ".in")
    output_path = path.join("./testcases", str(testcase_number) + ".out")
    input_pipe = open(input_path, "r")
    output_pipe = open(output_path, "w")
    run("a.exe", stdin=input_pipe, stdout=output_pipe)
    input_pipe.close()
    output_pipe.close()
