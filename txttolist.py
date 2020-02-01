import os

if os.path.isfile('savelog.txt'):
  log = []
  with open('savelog.txt', 'r') as f:
    for line in f:
      log.append(line.strip())

print(log)