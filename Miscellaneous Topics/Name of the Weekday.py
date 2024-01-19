from datetime import datetime
s=input()
o_b=datetime.strptime(s,"%d %b %Y")
result=o_b.strftime("%A")
print(result)
