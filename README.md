# AutoRelojControl

# Instalacion

### Paso 1: instalar selenium para python

pip install -U pyvirtualdisplay
pip install -U selenium

### Paso 2: Descargar el interface de navegador chrome

https://sites.google.com/a/chromium.org/chromedriver/downloads

hay encontraras los driver para tu version de chrome
se descargara como un zip al descomprimir encontraras con un binario
el cual debes colocar en la ruta que mas te convenga si usas linux o mac
hacer "chmod +x" para darle permisos de ejecucion

### Paso 3: Parametros

Debes hacer una copia del archivo Params.example.py y dejarlo como
Params.py, ahora editalo, colocale tus datos de inicio de sesion
ubicacion del chromeDriver y fechas feriadas

# Ejecucion

en una terminal ir a la carpeta donde esta el proyecto ejecutar

para Entrada:
python main.py IN

para Salida:
python main.py OUT

### Paso 4:

Si usas mac deberas ejecutar manualmente el proyecto hasta que ya no te pida permisos, casi siempre son en las dos primeras ejecuciones

### Paso 5:

colocalo en un crontab con las horas de entrada y salisa.

# Errores

- Debes verificar que la version del chrome sea la misma del chromeDriver
  ya que si tienes una versiona diferente no funcionara.
