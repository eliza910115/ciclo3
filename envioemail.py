from email.message import EmailMessage
import smtplib

def enviar_email(email_destino,codigo):
    remitente = "eblandon@uninorte.edu.co"
    destinatario = email_destino
    mensaje = "Codigo de Confirmacion"+codigo
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Codigo de Activacion" + codigo
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "W4t3r0615.")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

def recuperar_email(email_destino):
    remitente = "eblandon@uninorte.edu.co"
    destinatario = email_destino
    mensaje="<hr>"
    mensaje = "<h2>Recuperación de Cuenta</h2>"
    mensaje =mensaje+ "<a href='http://https://mensajeria-equipo6.herokuapp.com/restablecer/"+ email_destino +"'>Ingrese Aqui para restablecer su contraseña</a>" 
    mensaje=mensaje+"<hr>"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Recuperar Contraseña" 
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "W4t3r0615.")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()