import csv
import requests
from flask import Flask
from flask import request


   
   
app = Flask(__name__)

@app.route('/')
def index():
	return 'changed this'


@app.route('/towork/<current_time>')
def get_work(current_time):
		
		with open('santaclara.csv', 'r') as f:
		  reader = csv.reader(f)
		  your_list = list(reader)

		final_list = []
		total_len = len (your_list)
		x = 1 
		for x in range(1,total_len-1):

			time = ((your_list[x])[0])

			a = time
			l = list(a)
			index = 0
			letter = l[index]
			length = len (l)
			while (letter!=':'):
			  index += 1
			  letter = l[index]


			if (l[length-1]=='P'):
				if (index == 1):  
						hours = int(l[0])
						hours += 12
   
			if (index == 2):
				temphours = (l[0:2])
				hours = int(''.join(temphours))
				if (hours!=12):
					hours += 12

			if (l[length-1]=='A'):
				if (index == 1):  
					hours = int(l[0])
   
				if (index == 2):
					temphours = (l[0:2])
					hours = int(''.join(temphours)) 
					if (hours==12):
						hours -= 12
	
			minute = l[index:length-1]
  
			hours = list(str(hours))
			if (len(hours)==1):
				a = ['0']
				hours = a + hours


			finaltime = str(''.join(hours + minute))
			#print (finaltime)
			x +=1
	
			final_list.append(finaltime)
	
		#print (final_list)
	


		time_1 = current_time

		y = 1
		boolean = "false"
		while (boolean=="false"):
			time_2 = str(final_list[y])
			if (time_1<time_2):
				boolean = "True"
			else:
				y +=1
		
		z = 1
		reco_list = []
		for z in range (1,4):
			reco_time = str(final_list[y])
			reco_list.append(reco_time)
			z +=1
			y +=1
	
		print (reco_list)		
			# show the user profile for that user
		return 'Train timings %s' % reco_list

@app.route('/tohome/<current_time>')
def get_home(current_time):
		
		with open('mtnview.csv', 'r') as f:
		  reader = csv.reader(f)
		  your_list = list(reader)

		final_list = []
		total_len = len (your_list)
		x = 1 
		for x in range(1,total_len-1):

			time = ((your_list[x])[0])

			a = time
			l = list(a)
			index = 0
			letter = l[index]
			length = len (l)
			while (letter!=':'):
			  index += 1
			  letter = l[index]


			if (l[length-1]=='P'):
				if (index == 1):  
						hours = int(l[0])
						hours += 12
   
			if (index == 2):
				temphours = (l[0:2])
				hours = int(''.join(temphours))
				if (hours!=12):
					hours += 12

			if (l[length-1]=='A'):
				if (index == 1):  
					hours = int(l[0])
   
				if (index == 2):
					temphours = (l[0:2])
					hours = int(''.join(temphours)) 
					if (hours==12):
						hours -= 12
	
			minute = l[index:length-1]
  
			hours = list(str(hours))
			if (len(hours)==1):
				a = ['0']
				hours = a + hours


			finaltime = str(''.join(hours + minute))
			#print (finaltime)
			x +=1
	
			final_list.append(finaltime)
	
		#print (final_list)
	


		time_1 = current_time

		y = 1
		boolean = "false"
		while (boolean=="false"):
			time_2 = str(final_list[y])
			if (time_1<time_2):
				boolean = "True"
			else:
				y +=1
		
		z = 1
		reco_list = []
		for z in range (1,4):
			reco_time = str(final_list[y])
			reco_list.append(reco_time)
			z +=1
			y +=1
	
		print (reco_list)		
			# show the user profile for that user
		return 'Train timings %s' % reco_list

