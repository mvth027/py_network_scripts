import re

dhcpPool = '''

'''

interfaces = '''

'''

poolNameFind = ('ip dhcp pool (\S+)')
networkFind = ('network \w+.\w+.\w+.\w+ \w+.\w+.\w+.\w+')
defaultRouterFind = ('default-router (\w+.\w+.\w+.\w+)')
portChannelFind = ('Port-channel1.\d+')
IPinterfacesFind = ('100.\d+.\d+.\d+')
poolName = re.findall(poolNameFind, dhcpPool)
network = re.findall(networkFind, dhcpPool)
defaultRouter = re.findall(defaultRouterFind, dhcpPool)
portChannel = re.findall(portChannelFind, interfaces)
IPinterface = re.findall(IPinterfacesFind, interfaces)
intDict = dict(zip(IPinterface,portChannel,))
try:   
 i = 0
 while i <= len(poolName):
     print (str(poolName[i]))
     print (str(network[i]))
     print ("default-router " + str(defaultRouter[i]))
     print (str(intDict[defaultRouter[i]]))
     print ("")
     i += 1
except IndexError:
    print ('')
