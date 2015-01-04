-export([request/1]).

request(Req) ->
	myserver ! {self(),{request,Req}},
	receive
		{myserver,{reply,Rep}} ->
			Rep
	end.