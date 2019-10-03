option Explicit
Function wait(sec)
	Dim dteWait
  	dteWait = DateAdd("s", sec, Now())
	Do Until (Now() > dteWait)
	Loop
End Function
Dim obj
set obj = CreateObject("wscript.shell")
obj.run("cmd")
wait(4)
obj.sendkeys"inetcpl.cpl"
wait(1)
obj.sendkeys"{ENTER}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"L"
wait(1)
obj.sendkeys"x"
wait(1)								
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{ENTER}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{ENTER}"