import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    str_list = test.strip().split(' ')
    word_len = [len(item) for item in str_list]
    print str_list[word_len.index(max(word_len))]