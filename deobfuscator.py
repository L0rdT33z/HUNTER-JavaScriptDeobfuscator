from __future__ import unicode_literals
import re

_0xce1e="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"
def duf(d,e,f):
    g = list(_0xce1e)
    h = g[0:e]
    i = g[0:f]
    d = list(d)[::-1]
    j = 0
    for c,b in enumerate(d):
        if b in h:
            j = j + h.index(b)*e**c

    k = ""
    while j > 0:
        k = i[j%f] + k
        j = (j - (j%f))//f

    return int(k) or 0

def hunter(h,u,n,t,e,r):
    r = "";
    i = 0
    while i < len(h):
        j = 0
        s = ""
        while h[i] is not n[e]:
            s = ''.join([s,h[i]])
            i = i + 1

        while j < len(n):
            s = s.replace(n[j],str(j))
            j = j + 1

        r = ''.join([r,''.join(map(chr, [duf(s,e,10) - t]))])
        i = i + 1

    return r


code=input("Enter Hunter JS Obfuscated Code : ")

regex = r"\(\"([^)]+)\)"

matches = re.findall(regex, code, re.MULTILINE)[0]

code_list = matches.split(',')
for idx,code in enumerate(code_list):
	if code.isdigit():
		code_list[idx] = int(code)
	else:
		code_list[idx] = code.replace('\"','')

result = hunter(*code_list)
print(result)
