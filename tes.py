import re
text = 'Nomer ponsel saya adalah 0821-1228-8888'
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
results.group()
# 0821-1228-8888
results.group(1)
# 0821
results.group(2)
# 1228
results.group(3)
# 8888