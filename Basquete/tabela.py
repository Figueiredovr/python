# Victor Figueiredo 24/08/2015

# Esse programa lê um arquivo txt contendo uma lista com
# respectivamente: nome do jogador, pontos marcados
# e quantidade de cestas de 3 pontos. Ordena e retorna duas tabelas em hmtl


arquivo = open("pontos.txt","r") #arquivo de entrada
saida = open("cestinha.txt","w") #Jogadores que marcaram mais pontos
saida2 = open("3pontos.txt","w") #Jogadores com mais cestas de 3

lista = []
cestinha = []

#Leitura dos arquivos 
for line in arquivo :
	vetor = line.split()
	elemento = [(int(vetor[1])),(vetor[0])]   # Tupla ( Ponto, Nome)
	elemento2 = [(int(vetor[2])),(vetor[0])]  #Tupla (3 Pontos, Nome)
	lista.append(elemento)                    #Lista jogadores com mais pontos 
	cestinha.append(elemento2)                #Lista de jogadores com mais cestas de 3

# Ordenando e invertendo a lista
lista.sort()
lista.reverse()

cont = 0;

#Tabela html jogadores com mais pontos
for i in lista:
	cont+=1
	saida.writelines("<tr>\n")

	line = "   <th> " + str(cont)+ "&ordm;" + " </th>\n"
	saida.writelines(line)

	line = "   <th> " + i[1] + " </th>\n"
	saida.writelines(line)

	line = "   <th> " + str(i[0]) + " </th>\n"
	saida.writelines(line)

	saida.writelines("</tr>\n")

cont = 0

#Ordenando e invertendo a lista
cestinha.sort()
cestinha.reverse()

#Tabela html jogadores com mais cestas de 3
for i in cestinha:
	cont+=1
	saida2.writelines("<tr>\n")

	line = "   <th> " + str(cont)+ "&ordm;" + " </th>\n"
	saida2.writelines(line)

	line = "   <th> " + i[1] + " </th>\n"
	saida2.writelines(line)

	line = "   <th> " + str(i[0]) + " </th>\n"
	saida2.writelines(line)

	saida2.writelines("</tr>\n")




arquivo.close()
saida.close()
saida2.close()