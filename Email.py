import smtplib, imapclient

conn = smtplib.SMTP('smtp.gmail.com', 587)
print(str(conn.ehlo()))
conn.starttls()
conn.login('jefferyjohn2000@gmail.com', '**************')
conn.sendmail('jefferyjohn2000@gmail.com', 'Jeffery.John@uga.edu', 'Subject: Test\n\nHi Jeffery,\nYou sent this email to yourself!\n\n')
conn.quit()

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('jefferyjohn2000@gmail.com', '**************')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 25-March-2020'])
rawMessage = conn.fetch([99999], ['BODY[]', 'FLAGS'])
