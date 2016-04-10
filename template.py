import sys

name = "test"
path = ""

sys.stdin = open(path + name + ".in")
#sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input().split()
    ### start

    print("Case #" + str(testCase) + ": " + "0")