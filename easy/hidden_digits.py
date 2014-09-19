import sys
import re
 
test_cases = open(sys.argv[1], 'r') 
for test in test_cases:
    pattern = re.compile('[a-j0-9]')
    hidden_list = pattern.findall(test.strip())
    if not hidden_list:
    	print "NONE"
    	continue
    result = []
    for item in hidden_list:
    	if item >= 'a' and item <= 'j':
    		result.append(str(ord(item)-97))
    	else:
    		result.append(str(item))
    print ''.join(result)