import pywhatkit as kit 
from datetime import datetime 

data_atual = datetime.now()

# Enviando a mensagem instantaneamente

kit.sendwhatmsg_instantly("numero de telefone", "Teste de automação")

# Programado com um tempo para enviar a mensagem

kit.sendwhatmsg("numero de telefone", "Teste novamente usando o tempo", data_atual.hour, data_atual.minute + 2)