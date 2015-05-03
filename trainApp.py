import gtfs_realtime_pb2
import csv
import urllib2
import logging 

class trainTrip(object):
	"""docstring for trainTrip"""
	def __init__(self, arg):
		self.trip_id = trip_id
		self.route_id = route_id
		self.stop_id = None
		self.stop_sequence = 0
		self.status = None
		self.status_timestamp = None
		self.status_timestamp = None
		super(trainTrip, self).__init__()
		self.arg = arg

	def __repr__(self):
		return "[trip_id:{0}, " \
				"route_id:{1}," \
				"stop:{2}," \
		pass