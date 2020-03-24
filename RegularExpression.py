import re
import pprint

message = 'Call me if you have any questions about sponsoring UGAHacks at 678-531-8131'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search(message)
print(matchObject.group())

sponsorReply = 'My numbers are 123-456-7890 on M-F 8-5, but you can call me any time at 098-765-4321 ;)'
pprint.pprint(phoneNumRegex.findall(sponsorReply))
