name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict();
for line in handle:
    if line.startswith('From '):
        dic[line.split()[1]] = dic.get(line.split()[1],0) + 1;
largestCount = None
largestProlific = None
#dictionaries are mutable
#lists are mutable
for key,value in dic.items():
    if largestCount is None or value > largestCount:
        largestProlific = key
        largestCount = value
print(largestProlific, largestCount)
