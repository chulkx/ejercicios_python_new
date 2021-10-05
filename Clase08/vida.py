from datetime import datetime

#ejercicio 8.1
def vida_en_segundos(fecha_nac):
    
    '''Recibe la fecha de nacimiento en formato 'dd/mm/AAAA'
    y devuelve la cantidad de segundos transcurridos hasta ahora'''
    
    nac = datetime.strptime(fecha_nac, '%d/%m/%Y')
    hoy = datetime.now()

    return (hoy - nac).total_seconds()
