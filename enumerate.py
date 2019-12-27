people = ['Hal','Em','Others']
ages = [30,40,50]
nationalities = ['US','French','Unknown']
for person, age, who in zip(people, ages, nationalities):
	print (person, who, age)