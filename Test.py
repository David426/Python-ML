import os

input = "Tests/input_"
output = "Tests/output_"
extension = ".txt"
expected = "Expected: "
function = "python3 sbml.py "
sbml = "SBML output: "
for i in range(1, 40):
    inputFile = open(input + i.__str__() + extension, 'r')
    outputFile = open(output + i.__str__() + extension, 'r')
    expression = inputFile.read()
    expectedOutput = outputFile.read()
    print("\n" + input + i.__str__() + extension + " : "+ expression)
    print(expected + expectedOutput)
    print(sbml, end="")
    os.system(function + input + i.__str__() + extension)


