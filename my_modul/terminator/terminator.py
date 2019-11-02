s=[]
for x in range(10000):
	s.append("")

for x in  range(len(s)):
	for y in range(200):
		d = "spy_dir" + str(x) + str(y)
		s[x] = open("/home/{0}.txt".format(d)","w")
		for z in range(1000):
			s[x].write(str(z) + "/n")

