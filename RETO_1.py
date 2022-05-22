def CDT(usuario:str, capital:int, tiempo:int):
  cdt_intereses =((capital*0.03)* (tiempo)) / 12
  return cdt_intereses

def CDT2(usuario:str, capital:int, tiempo:int):
  cdtnegativo=((capital*0.02)*(tiempo)) / 12
  return cdtnegativo       

user= str(input ("Ingrese el usuario: "))   ##input por parte de los usaurios
cap= int(input ("Ingrese el monto del capital: "))
time= int(input ("Ingrese la cantidad de tiempo: "))

if (time >2):
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial: $" +str(cap),  
       "para un tiempo de "+str(time), "meses", "es de: "+ str(CDT(user,cap,time)),"%") 
##Se llama la variable y los datos del input con los cuales realizar la operacion
else:
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial: $" +str(cap),  
       "para un tiempo de "+str(time), "meses", "es de: "+ str(CDT2(user,cap,time)),"% Por tener el CDT menos tiempo") 

 