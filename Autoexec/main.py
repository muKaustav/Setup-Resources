with open('updateLib.txt') as f:
    lines = [line.rstrip() for line in f]

with open('script.bat', 'a') as out:
    for i in range(len(lines)):
        out.write("pip install " + lines[i].split( )[0] + " -U" + '\n')


