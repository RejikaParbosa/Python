players=open('tenis_player.txt','w')
players.write('Nobi Nobita\n')
players.write('Uzumaki Naruto\n')
players.write('Squid Girl\n')
players.close()

countries=open('tenis_countries.txt','w')
countries.write('Japan\n')
countries.write('Hidden Leaf Village\n')
countries.write('Oceania\n')
countries.close()

print(players)
print(countries)

n=open('tenis_player.txt','r')
c=open('tenis_countries.txt','r')
pn=[]
pc=[]
pn=n.read()#read all players
pc=c.read()
for l in n:
    pn.append(l[:-1])#ignore '\n'
    n.close()

for l in c:
    pc.append(l[:-1])
    c.close()
print(pn, '\n', pc)

name_country=[] #empty list
for i in range(len(pn)):
    name_country.append()
