
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
                wait(2)
                obj.sendkeys"python C:\Users\98912\Desktop\instagram\proxy-maker\a.py"
                obj.sendkeys"{ENTER}"
                