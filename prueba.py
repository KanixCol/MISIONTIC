def CDT(usuario:str, capital:int, tiempo:int):
  cdt_intereses =((capital*0.03)* (tiempo)) / 12
  return cdt_intereses

def CDT2(usuario:str, capital:int, tiempo:int):
  cdtnegativo=((capital*0.02)*(tiempo)) / 12
  return cdtnegativo       

user= str(("AB1012"))   ##input por parte de los usaurios
cap= int((1000000))
time= int((3))

user= str(("ER3366"))   ##input por parte de los usaurios
cap= int((650000))
time= int((2))

if (time >2): ##Se evalua el tiempo si es mayor a 2 meses ejecuta una funcion definida previamente o si es menor, imprime el mensaje despues de 
    #realizar las operaciones definididas en las funciones.  
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial " +str(cap),  
       "para un tiempo de "+str(time), "meses", "es: "+ str(CDT(user,cap,time)+ (cap))) 

else:
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial " +str(cap),  
       "para un tiempo de "+str(time), "meses", "es: "+ str(CDT2(user,cap,time) - (cap))) 

 