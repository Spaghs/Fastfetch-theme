import shutil
from math import floor

total, used, free = shutil.disk_usage("/")

total //= (2**30)
used //= (2**30)
#used = 430

perc = used/total * 100
percbar = floor(perc / 5)

bar = ""
bar += "■" * (percbar)
bar += "═" * (20-percbar)

print(f"{perc:.2f}%  {bar} {used}/{total} GiB")
