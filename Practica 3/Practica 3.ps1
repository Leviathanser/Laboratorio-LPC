function tabla1{

    for($i = 1; $i -lt 11; $i++){
        Write-Host $i 'x' $num '=' ($i*$num)
    }
}
Write-Host "`Tabla de multiplicar"
Write-Host " Solo numeros positivos"
[int]$num = [int](Read-Host -Prompt "Escribe un numero: ")

if($num -ge 0){
    tabla1($num)
}
else{
    Write-Host "El numero es negativo"
}