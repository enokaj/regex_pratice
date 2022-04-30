import re
import ipaddress


ip_regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
ip_list = []


def valid_ip(address):
    try: 
        ipaddress.ip_address(address)
        return True
    except:
        return False


with open("log.txt") as log_file:
    for item in log_file:
        ip = ip_regex.findall(item)
        if ip and ip[0] not in ip_list:
            if valid_ip(ip[0]) is True:
                ip_list.append(ip[0])


[print(x) for x in ip_list]