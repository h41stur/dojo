$ip = ((ipconfig | findstr [0-9].\.)[0]).Split()[-1].substring(0, 9)

For($i=0; $i -le 255; $i++){
    echo "`n"
    $hst = "$ip.$i"
    $test = Test-Connection -ComputerName $hst -Count 1 -Quiet
    if ( $test ) {
        echo "[-] $hst"
        1..65355 | % {echo ((new-object Net.Sockets.TcpClient).Connect($hst,$_)) "Porta $_ --- ABERTA"} 2>$null
    }
    
 }