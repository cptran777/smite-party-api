from django.core import serializers
from random import randint

def test():

	print 'Hello and fuck the job search'

def shuffle(arr):

	return 'test'

# Returns a list/array where the element(s) meets the criteria
def filter(arr, **kwargs):
	
	output = []

	for item in arr:
		for key in kwargs.keys():
			if (item.get(key, None) == kwargs[key]):
				output.append(item)
				break;

	return output

# Returns a single object that meets a criteria
def select(arr, **kwargs):
	
	key = kwargs.keys()[0]

	for item in arr:
		if (item.get(key, None) == kwargs[key]):
			return item

	return None 

# Randomizer is passed the gods and roles models to make queries
def randomizer(gods, roles): 

	# For the randomizer, we want to return a list (array) with each role
	# that has been shuffled to be randomly assigned

	# Algorithm:
	# Choose carry first, which will decide the filters for guardian
	# Choose mid third, which is decided by carry/guardian choices
	# Choose solo next, which is decided by the mid/carry choices
	# Choose jungler last, which can be affected by the solo choice

	output = []

	# Two database calls:
	roles_query = serializers.serialize('json', roles.objects.all())
	gods_query = serializers.serialize('json', gods.objects.all())

	# Choosing the carry:

	print 'testing filter: '
	myArray = [{'a': 5, 'b': 6}, {'b': 6, 'c': 3}, {'a': 5, 'c': 3}, {'a': 3, 'b': 6}]
	print filter(myArray, a = 5)
	print select(myArray, a = 3)

	# print randint(0, 10)

	return 7