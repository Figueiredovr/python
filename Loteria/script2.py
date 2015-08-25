#Victor Figueiredo

#Esse programa faz algumas análises como moda e outros
#nos resultados da lotomania

arquivo = open("resultados.txt","r")

count=0
result=[0]*100
for line in arquivo.readlines():
	if len(line)<5:
		result[int(line)] = result[int(line)] + 1

lista=[0]*100
x = range(100)
for i in range (100):
	lista[i] = (result[i],x[i])
#plot.bar(n, n**2, align="center", width=0.5, alpha=0.5)
lista.sort()
print(lista)
# print(result[10])
# print(result[12])
# print(result[13])
# print(result[15])
# print(result[17])
# print(result[21])
# print(result[22])
# print(result[27])
# print(result[40])
# print(result[61])
# print(result[67])
# print(result[68])
# print(result[75])
# print(result[85])
# print(result[88])
# print(result[92])
print("\nVinte e cinco maiores\n")

for i in range(25):
	print lista[i]