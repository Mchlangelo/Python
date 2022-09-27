#Gerador de Qrd code para um link específico
import qrcode           

link = qrcode.make("link de destino")
link.save("nome e extensão para salvar o qrcode (por ex: pode ser um png, jpg, etc...")