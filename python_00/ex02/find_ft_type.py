def all_thing_is_obj(object: any) -> int:

	obj_type = str(object.__class__)
	if obj_type == "<class 'list'>":
		print("List : <class 'list'>")
	elif obj_type == "<class 'tuple'>":
		print("Tuple : <class 'tuple'>")
	elif obj_type == "<class 'set'>":
		print("Set : <class 'set'>")
	elif obj_type == "<class 'dict'>":
		print("Dict : <class 'dict'>")
	elif obj_type == "<class 'str'>":
		if object == "Brian":
			print("Brian is in the kitchen : <class 'str'>")
		elif object == "Toto":
			print("Toto is in the kitchen : <class 'str'>")
		else:
			print("Type not found")
	elif obj_type == "<class 'int'>":
		print("Type not found")
		return 42
	else:
		print("Type not found")
	return 0

