import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
#for encryption
conn.starttls()
#Logging into the account
conn.login('#####@gmail.com','###pass###')
#sending mail
conn.sendmail('####@gmail.com','####@gmail.com','Subject: So long...\n\nDear All,\nSo Long and thanks fro all the fish....\n\n-poonam')
conn.quit()
