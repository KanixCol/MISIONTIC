def CDT(usuario:str, capital:int, tiempo:int):
       cdt_intereses = ((tiempo)* (capital*0.03)) / 12
       return cdt_intereses

user= str("AB1012")
cap= int(1000000)
time= int(3)

if (time >=2): ##Se evalua el tiempo si es mayor a 2 meses ejecuta una funcion definida previamente o si es menor, imprime el mensaje despues de 
    #realizar las operaciones definididas en las funciones.  
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial: " +str(cap),  
       "para un tiempo de "+str(time), "meses", "es "+ str(CDT(user,cap,time)+ (cap))) 

else:
 print ("Para el usuario " +user , "La cantidad de dinero a recibir, según el monto inicial: " +str(cap),  
       "para un tiempo de "+str(time), "meses", "es:"+ str(CDT(user,cap,time) - (cap))) 
