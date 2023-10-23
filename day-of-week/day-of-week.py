import sys,datetime as d
for t in sys.argv[1:]:print(d.datetime.strptime(t,'%Y-%m-%d').strftime('%A'))
