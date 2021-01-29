import os
import time
with open("host.txt") as file: 
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('#'*60)
        os.system(f'ping -n 2 {ip}')
        time.sleep(3)