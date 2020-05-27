import subprocess

scan = True
while scan:
    results = subprocess.check_output(['netsh', 'wlan',
     'show', 'network'])
    results = results.decode('ascii')
    results = results.replace('\r', '')
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    ssid_index = 0

    while ssid_index < len(ls):
        if ssid_index % 5 == 0:
            ssids.append(ls[ssid_index])
        ssid_index += 5

    for network in ssids:
        print(network)

    scan = input("Scan again? ")
    if not scan.lower().startswith('y'):
        scan = False            