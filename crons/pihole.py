import pihole as ph

pihole = ph.PiHole('172.16.10.5')

data = dict()
data['queries'] = ph.queries
data['blocked'] = ph.blocked
data['adds_percent'] = ph.ads_percentage

print(data)