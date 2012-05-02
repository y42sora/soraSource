a = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvzq"""
b = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upqz"""

l = dict([])
for (x,y) in zip(a,b):
 l[x] = y


f = open('text.txt', 'r')
o = open('out.txt', 'w')
f.readline()

num = 1

for line in f:
 s = line.rstrip()
 ans = ""
 for x in s:
  ans += l[x]
 o.write("Case #%d: %s\n" % (num, ans))
 num += 1

