#!/usr/bin/env python
#  python  module to query range server
#  Example usage 
#  #!/usr/bin/python
#  from range import expand
#  print expand("range hostname",9999,"@range_query")


import os,sys,socket
import requests

def expand(host,port,range_query):
  rport = 9999   # range port is set to 9999 by default
  if host:
    rhost = host
  elif resolv_hostname("range"):
    rhost = "range"
  else:
    rhost = get_environ_host()

  if port:
    rport = port
  else:
    rport = get_environ_port()

  if range_query:
    rquery = range_query
  else:  
    print "Range query is empty..exiting.."
    sys.exit()

  uri = 'http://%s:%d/range/list?%s' % (rhost, rport, rquery)
  try:
    result = requests.get(uri)
  except:
    print "A error occurred while quering..exiting"
    print e
    sys.exit()
  return result.content 
#  print sorted(result.content.splitlines()) 

def get_environ_host():
  if os.getenv('RANGE_HOST'):
    range_host = os.getenv('RANGE_HOST')
    return range_host
  else:
    print "range host is undefined.. please set RANGE_HOST env variable or pass range host to the module"
    sys.exit() 

def get_environ_port():
  if os.getenv('RANGE_PORT') is not None:
    range_port = os.getenv('RANGE_PORT')
    return range_port
  else:
    print "range port is undefined.. please set RANGE_PORT env variable or pass range port to the module (default 9999)"
    sys.exit() 

def resolv_hostname(hostname):
  try:
    socket.gethostbyname(hostname)
    return 1
  except socket.error:
    return None
