fread = open("cache.cfg", "r")
fwrite = open("cleanup", "a")

for line in fread:
    if line[0] == "-":
        fwrite.write(line)

fread.close()
fwrite.close()
    

