#tuples are immutable
#tuples assignment can be done in normal string assignment method
#tuple comparison is also like the most significant place comparison
#list comprehension must visit topic
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hourList = dict();
newList = list();
for line in handle:
    if line.startswith('From '):
        hr = line.split()[-2].split(':')[0]
        hourList[hr] = hourList.get(hr,0) + 1;
for k,v in sorted(hourList.items()):
    print(k,v)
