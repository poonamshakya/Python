import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl= True)
conn.login('######@gmail.com','####pass####')

#check folders in mailbox
#print(conn.list_folders())
conn.select_folder('INBOX',readonly=True)
conn.search(['ALL'])
rawmessage = conn.fetch([16180],['BODY[]','FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawmessage[16180][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))

#extract text part of mail
print(message.text_part.get_payload().decode('UTF-8'))

# extract html part of mail if present
#print(message.html_part.get_payload().decode('UTF-8'))
conn.logout()