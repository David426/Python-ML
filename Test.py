import os, sys, subprocess
input = "Tests/input_"
output = "Tests/output_"
extension = ".txt"
expected = "Expected   : "
function = "python3 sbml_old.py "
sbml = "SBML output: "
start = 1
stop = 41
count = 0
attempted = 0
if len(sys.argv) == 2:
    start = int(sys.argv[1])
    stop = int(start) + 1
elif len(sys.argv) == 3:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
for i in range(start, stop):
    attempted += 1
    inputFile = open(input + i.__str__() + extension, 'r')
    outputFile = open(output + i.__str__() + extension, 'r')
    expression = inputFile.read()
    expectedOutput = outputFile.read()
    print("\n" + input + i.__str__() + extension + " : "+ expression)
    print(expected + expectedOutput)
    print(sbml, end="")
    # sbmlOutput = subprocess.check_output(function + input + i.__str__() + extension, shell=True)
    sbmlOutput = os.popen(function + input + i.__str__() + extension).read()
    sbmlOutput = sbmlOutput[:len(sbmlOutput)-1]
    print(sbmlOutput)
    if sbmlOutput.lower() == expectedOutput.lower():
        count += 1
        print("CORRECT: " + count.__str__() + '/' + attempted.__str__())
    else:
        print("INCORRECT: " + count.__str__() + '/' + attempted.__str__())

print("TOTAL: " + count.__str__() + '/' + attempted.__str__())