@echo off
title Abrindo Analisador de PDF
:: Verifica se o Ollama está rodando, se não, avisa o usuário
tasklist /FI "IMAGENAME eq ollama app.exe" 2>NUL | find /I /N "ollama app.exe">NUL
if "%ERRORLEVEL%"=="1" (
    echo [AVISO] O Ollama nao parece estar aberto. Iniciando...
    start "" "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama app.exe"
)

echo Iniciando Interface Streamlit...
:: Substitua 'seu_script.py' pelo nome real do seu arquivo
streamlit run "leitorPDF.py"
pause