from google.transit import gtfs_realtime_pb2
import urllib 

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://web.mta.info/status/serviceStatus.txt')
feed.ParseFromString(response.read())
for entity in feed.entity:
	if entity.HasField('trip_update'):
		print entity.trip_update

		