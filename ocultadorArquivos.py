import ctypes
ocultar = 0x02 #Arquivo oculto
caminho = str(input('Digite o caminho do arquivo/pasta a ser ocultado: ')).strip().lower()
retorno = ctypes.windll.kernel32.SetFileAttributesW(caminho, ocultar)
if retorno:
    print('O arquivo foi ocultado.')
else:
    print('O arquivo não foi ocultado.')