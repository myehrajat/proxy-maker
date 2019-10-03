
                option Explicit
                Function wait(sec)
                    Dim dteWait
                    dteWait = DateAdd("s", sec, Now())
                    Do Until (Now() > dteWait)
                Loop
                End Function
                Dim obj
                set obj = CreateObject("wscript.shell")
                obj.run("cmd /c ")
                wait(2)
                