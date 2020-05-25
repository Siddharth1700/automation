import smtplib
host_name = "user_name@gmail.com"
host_pass = "password"
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("host_name","host_pass")
server.sendmail("host_name",
		"host_name",
		"jon is successfull"
server.quit()