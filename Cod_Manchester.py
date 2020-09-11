import numpy as np 
b=([])
c=([1,0,1,1,0,0,0,1,0,0,1,1]) #Aqui se recibe la cadena de texto antes codificada
d=([])

for i in c: #Inicia el ciclo para poder leer la lista y poder generar una nueva lista con la codificacion Manchester
	if i == 0:
		b.append(1)
		b.append(0)
	if i == 1:
		b.append(0)
		b.append(1)
print(b) #se imprime como quedara la lista despues de su codificacion manchester
if b[0]==0 and b[1]==1: #Empieza el proceso de decodificacion despues de haber recibido la cadena codificada
	d.append(1)
if b[0]==1 and b[1]==0:
	d.append(0)
if b[2]==0 and b[3]==1:
	d.append(1)
if b[2]==1 and b[3]==0:
	d.append(0)
if b[4]==0 and b[5]==1:
	d.append(1)
if b[4]==1 and b[5]==0:
	d.append(0)
if b[6]==0 and b[7]==1:
	d.append(1)
if b[6]==1 and b[7]==0:
	d.append(0)
if b[8]==0 and b[9]==1:
	d.append(1)
if b[8]==1 and b[9]==0:
	d.append(0)
if b[10]==0 and b[11]==1:
	d.append(1)
if b[10]==1 and b[11]==0:
	d.append(0)
if b[12]==0 and b[13]==1:
	d.append(1)
if b[12]==1 and b[13]==0:
	d.append(0)
if b[14]==0 and b[15]==1:
	d.append(1)
if b[14]==1 and b[15]==0:
	d.append(0)
if b[16]==0 and b[17]==1:
	d.append(1)
if b[16]==1 and b[17]==0:
	d.append(0)
if b[18]==0 and b[19]==1:
	d.append(1)
if b[18]==1 and b[19]==0:
	d.append(0)
if b[20]==0 and b[21]==1:
	d.append(1)
if b[20]==1 and b[21]==0:
	d.append(0)
if b[22]==0 and b[23]==1:
	d.append(1)
if b[22]==1 and b[23]==0:
	d.append(0)

print(d) #se imprime la decodificacion obtenida por manchester
print(c) #se imprime la cadena recibida para verificar que sea la misma.
