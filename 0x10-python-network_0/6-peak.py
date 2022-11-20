#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
	
	peak = None
	
	for i in range(len(list_of_integers)):
		if list_of_integers[i] >= list_of_integers[i + 1]:
			return list_of_integers[i]
	return list_of_integers[-1]
	
