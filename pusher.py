import os

commands = [
    'git init',
    'git add .',
    'git commit -m "firstcommit"',
    'git branch -M main',
    'git remote add origin https://github.com/bruteforcerxx/bruteforceportfolio1.git',
    'git push -u origin main'
]

for c in commands:
    cmm = os.popen(c)
    cmm = cmm.read()
    print(cmm)
