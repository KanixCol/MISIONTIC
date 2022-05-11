nombre= str(input("Ingrese nombre del alumno: "))
nota1=int(input("INGRESE LA NOTA 1 periodo: "))
nota2=int(input("INGRESE LA NOTA 2 periodo: "))
nota3=int(input("INGRESE LA NOTA 3 periodo: "))
nota4=int(input("INGRESE LA NOTA 4 periodo: "))

if ((nota1+nota2+nota3+nota4) <5):
   print("El alumno " +nombre, "NO PASO LA MATERIA, DEBE MATRICULAR DE NUEVO.")
   
elif ((nota1+nota2+nota3+nota4) ==5):
    print("El alumno " +nombre, "Entra en modo de mejoramiento para aprobar la materia.")
    
elif ((nota1+nota2+nota3+nota4) >5):
    print("El alumno " +nombre, "aprobó la materia.")

else: 
    print("USUARIO NO ASISTIO A CLASES")
    
  #Manejo de condicional anidado, se debe mejorar declaracion de variales y sus resultado
   

