from classes.Marking import Marking
from datetime import date
from Params import Params
import smtplib
import sys
import os.path

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
today = date.today()

if __name__ == '__main__':

	markType = sys.argv[1]

	if markType not in ['IN', 'OUT']:
		print('Argumento no valido, use IN o OUT')
		sys.exit()
	
	dateToday = today.strftime("%d-%m-%Y")
	
	if dateToday in Params.holidays:
		print('Dia feriado que lo disfrutes')
		sys.exit()


	for user in Params.users:
		marking = Marking(
			user["user"], 
			user["password"], 
			dirname, 
			markType,
			Params.driverPath
		)

		marking.mark()
		
