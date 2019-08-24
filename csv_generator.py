''' CSV generator '''

import random as rd

name = ["rocky",'bunty','raka', 'baba','parda']
address = ['luchow','dedhi','gulabganj','waterway','amrika']

data_count = int(input('data generator limit :  '))

for i in range(data_count):
	n = rd.choice(name)
	a = rd.choice(address)
	num = rd.randint(0,1000)
	e = f'{n}{num}@email.com'
	print('{}, {}, {}'.format(n,a,e))
