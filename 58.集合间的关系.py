#集合是否相等（集合是无序的序列）
#原理：元素相同就相等
s1={10,20,30,40}
s2={20,40,30,10}
print(s1==s2)
print(s1!=s2)
#集合间是否是子集关系调用 issubset方法判断
a={10,20,30,40}
b={10,20}
print(b.issubset(a))
#集合间是否是超集关系调用 issuperset方法判断
print(a.issuperset(b))
#集合间是否有交集关系调用 isdisjoint方法判断
print(a.isdisjoint(b))