unzipFolder := "C:\Users\" . A_UserName . "\AppData\Roaming\.minecraft\mods"
download := "C:\Users\" . A_UserName . "\Downloads"
rarFile := download . "\mods.rar"

Send, #r
Sleep % 500
SendInput % "{TEXT}" . "%appdata%\.minecraft\mods"
Send, {Enter}
Sleep % 1000
Send, ^a
Sleep % 500
Send, {Delete}
Sleep % 2000
RunWait, "C:\Program Files\WinRAR\WinRAR.exe" x "%rarFile%" "%unzipFolder%"
Sleep % 2000
WinClose, ahk_class CabinetWClass
Sleep % 1000
Msgbox % "成功安裝新模組，可以關閉此視窗了"
