def operacion(ganadas:int, perdidas:int, blanco:int):  ##Define la funcion y los paramteros a recibir
    total_puntos=(ganadas*4) +(perdidas*-1) +(blanco* 0)  ##nombre de la operacion y operacion de la funcion a realizar 
    return total_puntos  ##return del valor una vez realizaada la operacion anterior

pg= int(input ("ingrese preguntas Gandadas: "))   ##input por parte de los usaurios
pp= int(input ("ingrese preguntas perdidas: "))
pb= int(input ("ingrese preguntas respondidas en blanco: "))

print ("El puntaje definitivo del estudiante es: " + str(operacion(pg, pp, pb)))  ##print del resultado de la
#operacion de la def de la variable. 
 
 ##notas de usuario o estudiante. 
 