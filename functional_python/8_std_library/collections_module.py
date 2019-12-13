from collections import OrderedDict, deque, Counter, defaultdict
od = OrderedDict()

# ordered dict is subclass dict class so
# all the methods of dict class can be applicable to orddict
# It remembers tge oder of the keys in which order they were inserted
od['name'] = 'Anurag'
od['last'] = 'Gundappa'
od['phone'] = 9975753003
print(od)


# Double ended queue
# pythonic implementation of data structure dequeue
# it has methods to support both end insertion and deletions
# it looks like list but it is not, it is list like ds
d = deque()
# append
d.append(1)
d.append(2)
d.append(3)
d.append(1)
print(d)
# appendleft
d.appendleft(4)
d.appendleft(5)
d.appendleft(6)
print(d)
# clear
d.clear()
print(d)
# count
one = d.count(1)
print(one)
# extend
d.append(1)
d.append(2)
d.append(3)
d.append('abc')
print(d)
d.extend('abc')
d.extend([4, 5, 6])
print(d)
# pop
# remove last el from right right side
last = d.pop()
print(last)
# popleft
first = d.popleft()
print(first)
# remove
# it will first occurrence of given argument
d.remove(2)
print(d)


# Counter
# it returns a dict where the elments i iterable are keys and
# their occurrence is the value
c = Counter('Amravati')
print(c)
c = Counter([x for x in range(10)])
print(c)
el = c.elements()
print(el)
comm = c.most_common(3)
print(comm)


# DefaultDict
dd = defaultdict(list)
dd['name'] = 'Anurag'
dd['age'] = 30
print(dd)
print(dd['last'])
print(dd)
