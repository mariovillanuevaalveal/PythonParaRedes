# PythonParaRedes
Programación en python orientada a redes de datos. 

##Creación de entornos virtuales en Python. 

###Para Crear un entorno virtual. 

    Python3 -m venv micarpeta.

            crea si no existe el directorio micarpeta

###Activar el entorno virtual

  ####Para windows 
   
    micarpeta\Scripts\activate.bat
    
   ####Para linux y Mac    
   
    source micarpeta\bin\activate
    
###Para deactivar el entorno virtual 
    
    deactivate 

#Uso de PIP

MANEJO DE PAQUETES CON PIP

    se puede verificar que no existan paquetes adicionales de python instalados dentro del entoro virtual
        pip freeze
    
    Instalar un paquete dentro del entrono 
        pip3 install requests
    Para instalar una version especifica 
        pip3 install requests==2.6.0 
    
    Para actualizar una version 
        pip3 install --upgrade requests
    
    Para obtener informacion de paquete
        pip3 show requests
    
    Eliminar paquentes del entorno
        pip -m pip uninstall requests 
    
    revisar si el paque se encuentra nuevamente
        pip freeze / pip show requests
    
    Mostrar los paquetes instalados en un entorno virtual.
        pip list 
    
    Guardar en un archivo la lista de paquentes requerido.
        pip freeze > requirements.txt
    
    Instalar todos los paquetes requerido en un proyecto. 
        pip install -r requirements.txt
    
