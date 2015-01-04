-module(series).
-export([ap/3,gp/3,reverse/1,max/1,kv_init/0,kv_server/1,ap_server/0,ap_manager/0,code_stuff/0]).

ap(Start,_,1) -> Start;
ap(Start,Diff,N) when N>0 -> ap(Start+Diff,Diff,N-1).

gp(Start,_,1) -> Start;
gp(Start,Factor,N) when N>0 -> gp(Start*Factor,Factor,N-1).

reverse([H]) -> [H];
reverse([H|T]) -> reverse(T)++[H].

max([H]) -> H;
max([H|T]) ->
	Max = max(T),
	if
		Max>H -> Max;
		true -> H
	end.

kv_server(D) ->
	receive
		{put, Key, Val} ->
			Dnew = dict:store(Key,Val,D),
			kv_server(Dnew);
		{get,Client,Key} -> 
			Client ! dict:find(Key,D),
			kv_server(D);
		Any -> 
			io:format("Ignored ~p ~n", [Any]),
			kv_server(D)
	end.

kv_init() ->
	D = dict:new(),
	spawn(series,kv_server,[D]).

ap_server() ->
	receive
		{Sender,S,D,N} -> Sender ! {ok,ap(S,D,N)};
		_ -> io:format("Msg ignored")
	end,
	ap_server().

ap_manager() ->
	Pid = spawn_link(series,ap_server,[]),
	catch unregister(fac),
	register(ap,Pid),
	process_flag(trap_exit,true),
	receive
		{'EXIT',Pid,_} ->
			ap_manager();
		_ -> 
			io:put_chars("Quitting fac_manager\n")
	end.

% Generic Server Manager

manager(Name,Module,Func,Args) ->
	P = spawn_link(Module,Func,Args),
	process_flag(trap_exit,true),
	catch unregister(Name),
	register(Name,P),
	receive
		{'EXIT',P,_} ->
			io:format("Restarting ~p ~n",[Name]),
			manager(Name,Module,Func,Args);
		_ -> io:put_chars("Ignoring messages\n")
	end.

code_stuff() ->
	receive
		upgrade -> series:code_stuff();
		Msg -> io:format("Received new ~p ~n",[Msg]),
			code_stuff()
	end.