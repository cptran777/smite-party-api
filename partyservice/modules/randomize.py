from django.core import serializers
from random import randint

import json

def shuffle(arr):

	return 'test'

# Returns a list/array where the element(s) meets the criteria
# def filter(arr, **kwargs):
	
# 	output = []

# 	for item in arr:
# 		for key in kwargs.keys():
# 			if (item['fields'].get(key, None) == kwargs[key]):
# 				output.append(item)
# 				break;

# 	return output

# Returns a function to be passed to the filter function
def filter_function(**kwargs):

	def output(item):
		for key in kwargs.keys():
			if item['fields'].get(key, None) == kwargs[key]:
				return True
		return False

	return output

# Does the same thing as filter for an array of objects/dicts, but
# with the added criteria of if the object's field name has a value
# contained in a list denoted by keyword = value
# can be passed a props for nested properties
def filter_by_list(arr, prop, **kwargs):

	output = []

	if prop: 
		for item in arr:
			for key in kwargs.keys():
				if item[prop].get(key, None) in kwargs[key]:
					output.append(item)
					break;
	else: 
		for item in arr:
			for key in kwargs.keys():
				if item.get(key, None) in kwargs[key]:
					output.append(item)
					break;

	return output

# Returns a single object from an array/list if it has a property
# denoted by keyword in its fields that meets the criteria
def select(arr, **kwargs):
	
	key = kwargs.keys()[0]

	for item in arr:
		if item['fields'].get(key, None) == kwargs[key]:
			return item

	return None

# Helper to return a random element from an array
def rand_select(arr): 

	return arr[randint(0, len(arr) - 1)]

# Randomizer is passed the gods and roles models to make queries
def randomizer(gods, roles): 

	# For the randomizer, we want to return a list (array) with each role
	# that has been shuffled to be randomly assigned

	# Algorithm:
	# Choose carry first, which will decide the filters for guardian
	# Choose mid third, which is decided by carry/guardian choices
	# Choose solo next, which is decided by the mid/carry choices
	# Choose jungler last, which can be affected by the solo choice

	output = {}

	# Two database calls:
	roles_query = json.loads(serializers.serialize('json', roles.objects.all()))
	gods_query = json.loads(serializers.serialize('json', gods.objects.all()))

	# Choosing the carry:
	carry_list = select(roles_query, role_name = 'Carry')['fields']['role_gods']
	gods_list = filter_by_list(gods_query, None, pk = carry_list)
	output['carry'] = rand_select(gods_query)

	# Choosing the guardian:
	# The guardian should simply be the opposite type from the carry
	support_filter = None
	if output['carry']['fields'].get('god_type', 0) == 'Physical':
		support_filter = 'Magical'
	else:
		support_filter = 'Physical'

	support_list = select(roles_query, role_name = 'Support')['fields']['role_gods']
	gods_list = filter(filter_function(god_type = support_filter), filter_by_list(gods_query, None, pk = support_list))

	print output['carry']['fields'].get('god_type', 0)

	print gods_list
	# output['carry'] = rand_select()

	# print randint(0, 10)

	return 7