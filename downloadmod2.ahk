unzipFolder := "C:\Users\" . A_UserName . "\AppData\Roaming\.minecraft\mods"
download := "C:\Users\" . A_UserName . "\Downloads"
rarFile := download . "\mods.rar"
defaultOutputFolder := unzipFolder
defaultRarFile := rarFile

Gui, Add, Text, x20 y20 w100 h20, RAR 檔案:
Gui, Add, Edit, vSelectedFile x130 y20 w200 h20, %defaultRarFile%
Gui, Add, Button, x350 y20 w80 h20 gSelectFile, 選擇檔案

Gui, Add, Text, x20 y50 w100 h20, 解壓縮位置:
Gui, Add, Edit, vOutputFolder x130 y50 w200 h20, %defaultOutputFolder%
Gui, Add, Button, x350 y50 w80 h20 gSelectOutputFolder, 選擇位置
Gui, Add, Button, x200 y80 w150 h30 gSetDefaultFolder, 預設位置

Gui, Add, Button, x20 y80 w150 h30 gInstall, 開始安裝

Gui, Show, w450 h120, 自動安裝模組工具 V2.0

Return

SelectFile:
    FileSelectFile, SelectedFile, , , 開啟檔案, RAR壓縮檔 (*.rar)
    if (SelectedFile != "")
    {
        GuiControl, , SelectedFile, %SelectedFile%
    }
    Return

SelectOutputFolder:
    FileSelectFolder, OutputFolder, , 3, 選擇解壓縮位置
    if (OutputFolder != "")
    {
        GuiControl, , OutputFolder, %OutputFolder%
    }
    Return

SetDefaultFolder:
    GuiControl, , OutputFolder, %defaultOutputFolder%
    GuiControl, , SelectedFile, %defaultRarFile%
    Return

Install:
    GuiControlGet, SelectedFile
    GuiControlGet, OutputFolder

    if (SelectedFile = "") {
        MsgBox, 沒有選擇壓縮檔
        Return
    }
    
    if (OutputFolder = "")
    {
        OutputFolder := defaultOutputFolder
    }

    Send, #r
    Sleep, 500
    SendInput, {TEXT}%appdata%\.minecraft\mods
    Send, {Enter}
    Sleep, 1000
    Send, ^a
    Sleep, 500
    Send, {Delete}
    Sleep, 2000
    RunWait, "C:\Program Files\WinRAR\WinRAR.exe" x "%SelectedFile%" "%OutputFolder%"
    Sleep, 2000
    WinClose, ahk_class CabinetWClass
    Sleep, 1000
    MsgBox, 成功安裝新模組，可以關閉此視窗了
    Return

GuiClose:
    ExitApp
    Return
