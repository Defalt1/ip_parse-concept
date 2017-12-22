

ip = []

ip_hosts = [192, 255, 255, 1]
ip_hosts_config = '.'.join(str(i) for i in ip_hosts)


def address():
  while len(ip) != 4:
    ip_input = input("Input IP address: ")
    if len(ip_input) > 3:
      print("Please input a valid IP address")
      continue
    elif len(ip_input) < 1:
      print("Please input a valid IP address")
      continue
    else:
      ip.append(ip_input)
  
  return (ip)
  
ips = '.'.join(str(i) for i in address())



if ips[0] == ip_hosts_config[0]:
  print("*Shared Hosting!*")
  print("Home Network " + '.'.join(ip) + " : " + "Shared Network " + (ip_hosts_config))
else:
  print("*Not a shared hosting*")
  print("Home Network " + '.'.join(ip) + " : " + "Other Network " + (ip_hosts_config))





