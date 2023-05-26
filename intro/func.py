l=["a","b","c"]
l +=["d"]
#print(len(l))

x="abc"
x*=2
#print(len(x))
n=[9,8,7,6,5]
n.append(4)
n.insert(2,11)
#print(len(n))

list=[8,4,2,6]
list.remove(2)
#print(len(list)+list.count(6))

nms=[2,4,8,9,5]
nms.insert(1,3)
nms.remove(9)
nms.insert(0,nms.count(8))
print(nms[3])