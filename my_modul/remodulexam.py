from re import findall,match,search,finditer
a="""mr reza
mr ali
mr.hoseyn"""
match=finditer(".*[^\s]",a)
for x in match:
    print(x.span(),a[x.span()[0]:x.span()[1]])
