code = {
		'а':'01','б':'02',
		'в':'03','г':'04',
		'д':'05','е':'06',
		'ё':'07','ж':'08',
		'з':'09','и':'0A',
		'й':'0B','к':'0C',
		'л':'0D','м':'0E',
		'н':'0F','о':'10',
		'п':'11','р':'12',
		'с':'13','т':'14',
		'у':'15','ф':'16',
		'х':'17','ц':'18',
		'ч':'19','ш':'1A',
		'щ':'1B','ъ':'1C',
		'ы':'1D','ь':'1E',
		'э':'1F','ю':'20',
		'я':'21',' ':'22'
		}


user = input('Введите букву, слово или предложение: ')

slova = ' '

for val in user:
	for item1, item2 in code.items():
		if item1 == val:
			slova = slova + item2 
			slova = slova + ' '
			break
		elif item1 != val:
			print('Даный символ не найден в словаре')
		
print('------------Результат------------')
print(slova)
print('---------------------------------')










