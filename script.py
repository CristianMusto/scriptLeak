import requests, os

dirPath = input("metti il path della cartella: \n")  
os.system(f"mkdir {dirPath}")

leaks = []

paths = open("paths.txt", "r").readlines()

for i in range(len(paths)):
    string = paths[i]
    trimmedString = string.rsplit(' ', 2)[0]
    leaks.append(trimmedString)


url = f"http://lockbitapt2d73krlbewgv27tquljgxr33xbwwsp6rkyieto7u4ncead.onion/ajax/listing-post?file-download=true&post=gU1S5nx0ZmVw4nU763a1980f779b1&path={leaks[0]}"
pdfs = requests.get(url)
print(pdfs.status_code)
print(pdfs)
os.system(f"mv {pdfs} {dirPath}")


