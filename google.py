from google import search

for resultado in search('"curso em video" google', stop=10):
    print(resultado)

