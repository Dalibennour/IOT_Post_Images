
from controllers import *
from tornado.web import url
route = [
		url(
			r"/" ,
			home.homeHandler #frant
		),
		
		url(
			r'/websocket', 
			home.stream_request_handler #serv
		),
	
]
					