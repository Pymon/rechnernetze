import ipaddress

rt = {
    "entries":[
        {"target": ipaddress.ip_network("134.109.192.0/24"), "gateway": ipaddress.ip_address("0.0.0.0"), "interface": "eth0"},
        {"target": ipaddress.ip_network("10.0.0.0/8"), "gateway": ipaddress.ip_address("134.109.192.23"), "interface": "eth0"},
        {"target": ipaddress.ip_network("192.168.0.0/16"), "gateway": ipaddress.ip_address("0.0.0.0"), "interface": "eth1"},
        {"target": ipaddress.ip_network("120.34.23.128/25"), "gateway": ipaddress.ip_address("192.168.23.47"), "interface": "eth1"},
    ],
    "default":
        {"target": "default", "gateway": ipaddress.ip_address("134.109.192.254"), "interface": "eth0"},
}


def find_in_rt(ip: ipaddress.IPv4Address):
    for entry in rt.get("entries"):
        if ip in entry.get("target"):
            print(entry.get("gateway"), entry.get("interface"))
            return
    print(rt.get("default").get("gateway"), rt.get("default").get("interface"))

while True:
    ip = input()
    try:
        ip =ipaddress.ip_address(ip)
    except Exception as e:
        print(str(e))
        continue
    if ip == "127.0.0.1":
        print("0.0.0.0 lo")
        continue
    find_in_rt(ip)
    
    