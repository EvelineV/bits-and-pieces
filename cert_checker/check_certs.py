import socket
import ssl
import datetime
import json


def ssl_expiry_datetime(hostname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(3.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)


with open("domains.json", "r") as f:
    domains_list = json.loads(f.read())["domains"]

for domain in domains_list:
    cert_expiry = ssl_expiry_datetime(domain)
    print(domain, ":", (cert_expiry-datetime.datetime.now()).days, "days left")
