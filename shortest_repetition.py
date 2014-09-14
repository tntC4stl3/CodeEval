import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    string = test.strip()
    length = len(string)
    for i in range(length):
 		if (i + 1) * string.count(string[:i+1]) == length:
 			print i + 1
 			break