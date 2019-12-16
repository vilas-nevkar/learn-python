import re

pat = re.compile(r"(\S+\s+\d+\s\d+:\d+:\d+)")
line = "Dec  7 02:40:02 10.10.50.2 8938: Dec  7 02:40:01.651 EST: %LINK-3-UPDOWN: Interface FastEthernet0/1/1, changed state to up"
match = re.findall(pat, line)
print(match[0])
