import subprocess

# Comando para abrir una nueva terminal en Windows
comando_terminal = 'cmd.exe'

# Ejemplo de código que quieres ejecutar en la nueva terminal
codigo_a_ejecutar = 'help' 
# Abre una nueva terminal y ejecuta el código
subprocess.Popen([comando_terminal, '/k', codigo_a_ejecutar])


