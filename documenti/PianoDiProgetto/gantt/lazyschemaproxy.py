#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class LazyTaskProxy(object):
	__slots__ = ["_obj", "_task_id", "_location"]

	def __init__(self, task_id, location):
		object.__setattr__(self, "_obj", None)
		object.__setattr__(self, "_task_id", task_id)
		object.__setattr__(self, "_location", location)

	def __load(self):
		if object.__getattribute__(self, "_obj") is None:
			location = object.__getattribute__(self, "_location")
			task_id = object.__getattribute__(self, "_task_id")
			object.__setattr__(self, "_obj", location.getTask(task_id))

	#
	# proxying (special cases)
	#
	def __getattribute__(self, name):
		if name == "id":
			return object.__getattribute__(self, "_task_id")
		else:
			self.__load()
			return getattr(object.__getattribute__(self, "_obj"), name)

	def __setattr__(self, name, value):
		self.__load()
		setattr(object.__getattribute__(self, "_obj"), name, value)
	
	def __nonzero__(self):
		self.__load()
		return bool(object.__getattribute__(self, "_obj"))
	def __str__(self):
		self.__load()
		return str(object.__getattribute__(self, "_obj"))
	def __repr__(self):
		self.__load()
		return repr(object.__getattribute__(self, "_obj"))
    