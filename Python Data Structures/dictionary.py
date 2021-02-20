name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict();
for line in handle:
    if line.startswith('From '):
        dic[line.split()[1]] = dic.get(line.split()[1],0) + 1;
(largestCount, largestProlific) = (None, None)
#dictionaries are mutable
#lists are mutable
for key,value in dic.items():
    if largestCount is None or value > largestCount:
        largestProlific = key
        largestCount = value
print(largestProlific, largestCount)

#dictionary items are not of the same order as inserted
#dict.keys() it gives the keys of dict in list format
#dict.values() it gives the values of dict in list format
#dict.items() it gives the key value pairs as items in list format that is each element of this list is a tuple in itself
