# SISTEMA de Categorização de IA para e-mails
Um sistema inteligente de automação que utiliza IA generativa para processar, filtrar e categorizar e-mails (em texto ou PDF), identificando solicitações produtivas e sugerindo respostas automáticas para otimizar o fluxo de atendimento.

# Como Utlizar o Projeto Localmente
Para rodar o programa localmente, é necessário ter instalado o FastApi e uma extensão que coloca o arquivo HTML na rede, que no caso do VSCode é a extensão GoLive

Para instalar o FastApi, digite no terminal:
- pip install fastapi[standard]

Será necessário modificar, no arquivo JavaScrip, a URL de execução do sistema, já que atualmente ele está configurado para funcionar no Vercel com Deploy de forma automatizada. Para isso, modifique a linha 35 de fetch para a URL de Teste, usando a variável URL_API_Teste = 'http://127.0.0.1:8000/categorizar'


- De:
  
        const response = await fetch("/categorizar", {

- Para:
  
        const response = await fetch(URL_API_Teste, {


  Também será necessário modificar o aquivo index.html do Frontend, alterando os endereços dos arquivos CSS e JS. Para isso na linha 7 do arquivo index.html, modifique:


- De:

      <link rel="stylesheet" href="/assets/css/style.css"> 

- Para:

      <link rel="stylesheet" href="assets/css/style.css"> 


  Da mesma forma, na linha 48 do arquivo index.html, modifique:

De:
  
    <script src="/assets/js/script.js"> </script>

Para:

    <script src="assets/js/script.js"> </script>


Por fim, rode a aplicação FastApi com o comando:
fastapi dev

E simultaneamente coloque o arquivo index.html na rede local e conseguirá utilizar o projeto.
