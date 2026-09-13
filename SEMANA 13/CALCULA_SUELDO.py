#declara la función
def calcular_sueldo(precio_horatrabajo: float, cantidad_horatrabajo: float) -> float:
    """
    CALCULA EL SALARIO A GANAR EN UN DÍA DEPENDIENDO DEL 
    PRECIO DE HORA Y LAS HORAS QUE TRABAJE EN ESE DÍA 
    VALORES QUE SERÁN INGRESADOS
    """
    total = precio_horatrabajo * cantidad_horatrabajo
    return total #retorno de resultado mediante la función
print("\n************* CALCULAR EL SUELDO DIARIO *************")

if __name__ == "__main__": # llamamos a la función
    # la función recibe los datos y los almacena en variables
    print("")
    precio_horatrabajo = float(input("INGRESE EL PRECIO DE LA HORA DE TRABAJO  "))
    cantidad_horatrabajo = float(input("INGRESE LAS CANTIDAD DE HORAS TRABAJADAS   "))
  
    # calculo realizado dentro de la función
    resultado = calcular_sueldo(precio_horatrabajo, cantidad_horatrabajo)

    # mostramos el resultado en consola mediante "print"
    print("\n**********************************************")
    print(f"  EL DIA DE HOY USTED HA GANADO: ${resultado:.2f}")
    print("\n**********************************************")