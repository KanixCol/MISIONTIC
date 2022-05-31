def CDT(usuario:str, capital:int, tiempo:int):
  if(tiempo<=2):
       cdt_intereses =((capital*0.02))
  else:cdt_intereses =((capital*0.03)* (tiempo)) / 12
  return cdt_intereses

user= str(input ("Ingrese el usuario: "))   ##input por parte de los usaurios
cap= int(input ("Ingrese el monto del capital: "))
time= int(input ("Ingrese la cantidad de tiempo: "))

if (time >2): ##Se evalua el tiempo si es mayor a 2 meses ejecuta una funcion definida previamente o si es menor, imprime el mensaje despues de 
    #realizar las operaciones definididas en las funciones.  
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial: " +str(cap),  
       "para un tiempo de "+str(time), "meses", "es "+ str(CDT(user,cap,time)+ (cap)))
else:
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial: " +str(cap),  
       "para un tiempo de "+str(time), "meses", "es:"+ str((cap) - CDT(user,cap,time))) 

 