import smtplib
import email.message
import datetime
import time

# Função para enviar e-mail
def enviar_email(email_destinatario, mensagem, nome):  
    corpo_email = f"""
    <html>
    <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9;">
        <div style="max-width: 600px; margin: 20px auto; background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden;">
            <div style="background-color: #b30000; color: #ffffff; text-align: center; padding: 20px 10px;">
                <h1 style="margin: 0; font-size: 24px;">🎄 Feliz Natal, {nome}! 🎁</h1>
            </div>
            <div style="padding: 20px; color: #333;">
                <p style="font-size: 18px; line-height: 1.6;">{mensagem}</p>
                <p style="font-size: 18px; line-height: 1.6;">Boas festas e um próspero Ano Novo para você! 🌟</p>
            </div>
            <div style="background-color: #1eb300; color: #ffffff; text-align: center; padding: 10px;">
                <p style="margin: 0; font-size: 14px;">Com carinho, <br><strong>Leonardo</strong></p>
            </div>
        </div>
    </body>
</html>

    """

    msg = email.message.Message()
    msg['Subject'] = "Boas Festas! 🌟"
    msg['From'] = ''
    msg['To'] = email_destinatario
    password = ''

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {email_destinatario} com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail para {email_destinatario}: {str(e)}')
    finally:
        s.quit()

# Função para carregar os dados do arquivo .txt
def carregar_dados(arquivo_txt):
    pessoas = []
    with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]  # Remove linhas vazias
        if len(linhas) % 3 != 0:
            raise ValueError("O arquivo não está formatado corretamente. Cada registro deve ter 3 linhas.")
        
        for i in range(0, len(linhas), 3):  # Cada registro tem 3 linhas
            nome = linhas[i]
            email_destinatario = linhas[i+1]
            # Tenta extrair a mensagem após ':'
            try:
                mensagem = linhas[i+2].split(':', 1)[1].strip()  # Remove "Mensagem:"
            except IndexError:
                raise ValueError(f"A linha de mensagem está formatada incorretamente: {linhas[i+2]}")
            pessoas.append((nome, email_destinatario, mensagem))
    return pessoas


# Checagem contínua
if __name__ == "__main__":
    print("Aguardando o dia 25 de desembro para enviar os e-mails...")
    while True:
        hoje = datetime.datetime.now()
        # Verifica se hoje é 30 de novembro
        if hoje.month == 12 and hoje.day == 25:
            print("Hoje é 30 de novembro! Enviando os e-mails...")
            dados = carregar_dados('emails.txt')
            for nome, email_destinatario, mensagem in dados:
                enviar_email(email_destinatario, mensagem, nome)
            break  # Sai do loop após enviar os e-mails
        else:
            # Aguarda 1 hora antes de checar novamente
            print("não é natal!")
            time.sleep(5)
           
