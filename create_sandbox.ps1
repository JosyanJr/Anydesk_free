Param(
    [string]$BoxName = "AnyDeskBox"
)

# Caminho padrão do Sandboxie-Plus
$SbieCtrlPath = "C:\Program Files\Sandboxie-Plus\SbieCtrl.exe"

# Verifica se a sandbox já existe
$existingBoxes = & $SbieCtrlPath /list | Select-String $BoxName
if ($existingBoxes) {
    Write-Output "Sandbox $BoxName já existe"
    exit
}

# Cria a sandbox com configurações avançadas
& $SbieCtrlPath /create /box:$BoxName

# Ativa Compartimento de Aplicativo e Proteção de Dados
# A configuração default da sandbox criada via CLI já aplica proteção de dados básica
# Para ajustes avançados é recomendado usar XML de configuração do Sandboxie
Write-Output "Sandbox $BoxName criada com sucesso"
