import sys
#usage: python logparse.py test.log
def parseLog(logfile):
	with open(logfile) as f:
		loglines = f.readlines()
		ipList = []
		for l in loglines:
			ip = l.split()[0]
			if ip not in ipList:
				ipList.append(ip)
		
		for i in ipList: # For debug
			print(i)     # For debug
	return ipList

if len(sys.argv) > 1:
	parseLog(sys.argv[1])