''' CSV generator '''

import random as rd

name = ["rocky",'bunty','raka', 'baba','parda']
address = ['luchow','dedhi','gulabganj','waterway','amrika']

data_count = int(input('data generator limit :  '))
delimiter  = input('Enter delimiter ("," is default):  ')
if delimiter == None or delimiter == ",":
	delimiter = ","

filename = input("enter filename  :")
filename += ".csv"

with open(filename,"w") as file:
	for i in range(data_count):
		n = rd.choice(name)
		a = rd.choice(address)
		num = rd.randint(0,1000)
		e = f'{n}{num}@email.com'
		dumdum = '{}{}{}{}{}'.format(n,delimiter,a,delimiter,e)
		file.writelines(dumdum + '\n')
