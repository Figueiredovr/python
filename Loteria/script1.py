# Victor Figueiredo

#Esse programa lê um arquivo hmtl com os resultados da lotomania
# e retorna um txt apenas com as datas e os resultados.

arquivo = open("D_LOTMAN.HTM","r")
arquivo2 = open("saida.txt","w")
arquivo3 = open("saida2.txt","w")

#Retirando as tags html
for line in arquivo.readlines():
	line2=""
	ctr=False
	for char in line:
		if char=="<":
			char=""
			ctr=True;
		elif char==">":
			char=""
			ctr=False
		if ctr:
			char=""

		
		line2= line2 + char

	arquivo2.writelines(line2)

arquivo2.close()
arquivo2 = open("saida.txt","r")

count=1
count2=0
ctr=False
arquivo2.readline()

#Retirando as "/"
for line in arquivo2.readlines():
	if len(line)>3:
		if line[2] =="/":
			ctr=False
			count = 0

	if ctr==True:
		line=""

	elif ctr==False:
		count = count+1
	
	if count == 21:
		ctr=True
		
		
	arquivo3.writelines(line)


arquivo.close()
arquivo2.close()
arquivo3.close()