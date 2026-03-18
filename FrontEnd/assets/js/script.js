URL_API_Teste = 'http://127.0.0.1:8000/categorizar'

document.getElementById('aiForm').addEventListener('submit', async function(e) {
    
    e.preventDefault();
    const fileInput = document.getElementById('fileInput');
    const textInput = document.getElementById('textInput');
    const statusMessage = document.getElementById('statusMessage');
    const submitBtn = document.getElementById('submitBtn');

    //Garante que o usuário envie pelo menos 1 arquivo ou corpo de email
    if (fileInput.files.length === 0 && textInput.value.trim() === '') {
        statusMessage.textContent = 'Por favor, anexe um arquivo ou insira um texto.';
        statusMessage.className = 'error';
        return;
    }

    const formData = new FormData();
    
    if (fileInput.files.length > 0) {
        formData.append('arquivo', fileInput.files[0]);
    }
    
    if (textInput.value.trim() !== '') {
        formData.append('corpo_email', textInput.value.trim());
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Enviando...';
    statusMessage.textContent = 'Processando com a IA...';
    statusMessage.className = 'loading';

    try {

        const response = await fetch("/categorizar", {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();
            statusMessage.textContent = 'Enviado com sucesso! IA analisou os dados.';
            statusMessage.className = 'success';
            console.log('Resposta da IA:', result);
            document.getElementById('box-resultado').style.display = 'block';

            const badgeCategoria = document.getElementById('badge-categoria');
            badgeCategoria.textContent = result.categoria;
            
            // Modifica a tela para se adequar a resposta de IA
            // Verde se a resposta foi Produtiva
            // Escala de Cinza se a resposta foi Improdutiva
            if (result.categoria.toUpperCase() === 'PRODUTIVO') {
                badgeCategoria.style.backgroundColor = '#4CAF50';
                badgeCategoria.style.color = 'white';
            } else {
                badgeCategoria.style.backgroundColor = '#9e9e9e';
                badgeCategoria.style.color = 'white';
            }

        const textoResposta = document.getElementById('texto-resposta-ia');
        textoResposta.value = result.resposta_ia;

        const btnCopiar = document.getElementById('btn-copiar');

        // Coloca o botão Copiar a disposição do usuário
        // Caso o usuário clique, a tela voltará ao normal depois de 2 segundos
        btnCopiar.onclick = () => {

            navigator.clipboard.writeText(result.resposta_ia)
            .then(() => {

                btnCopiar.textContent = '✅ Copiado!';
                btnCopiar.style.backgroundColor = '#d4edda';
                
                setTimeout(() => {
                    btnCopiar.textContent = '📋 Copiar Resposta';
                    btnCopiar.style.backgroundColor = '';
                }, 2000);
            })
            .catch(err => {

                console.error('Erro ao copiar texto: ', err);
                alert('Falha ao copiar. Tente selecionar o texto e dar Ctrl+C.');
            });
    };

        } else {
                throw new Error('Falha na resposta do servidor');
            }

        } catch (error) {
            console.error('Erro no envio:', error);
            statusMessage.textContent = 'Erro ao enviar para a IA. Verifique a conexão.';
            statusMessage.className = 'error';

        } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Enviar para IA';
                
            }
        });