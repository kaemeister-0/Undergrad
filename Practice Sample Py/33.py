t=int(input('seconds ='))

h = t // 3600
hs = t % 3600
m = hs // 60
s = hs % 60
print('%s Hours %s Minutes %s Seconds'%(h,m,s))