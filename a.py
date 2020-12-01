import re

a = '古朗月行 [唐] 李白==='
b = re.match('.*(\s+\[)', a)

print(b.groups())