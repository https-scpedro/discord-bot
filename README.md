### 📜 Sobre o Projeto
Esse bot nasceu como um projeto de estudo em Python, com o objetivo de explorar a criação de bots para Discord utilizando a biblioteca discord.py. O que começou com um simples comando de música evoluiu para um bot com uma estrutura organizada em Cogs, tratamento de erros e uma base sólida para futuras expansões.
Este repositório documenta não apenas o código, mas também a jornada de aprendizado, os desafios de depuração e as soluções encontradas ao longo do caminho.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Biblioteca Principal:** discord.py
* **Reprodução de Áudio e Mídia:** yt-dlp e FFmpeg
* **Variáveis de Ambiente:** python-dotenv

### ✨ Funcionalidades Atuais
Atualmente, o foco principal do bot é a reprodução de músicas, com os seguintes recursos já implementados:
* **Reproducao de musicas:** Toca músicas diretamente do YouTube através de um link ou de uma busca pelo nome.
* **Conexao Inteligente:** O bot entra automaticamente no canal de voz do usuário que executou o comando.
* **Auto-Deafen:** O bot se silencia (deafen) ao entrar no canal, mantendo a privacidade dos usuérios, além de economizar banda e não causar eco.
* **Desconexão por Inatividade:** Para não ficar ocupando um canal desnecessariamente, o bot se desconecta após 5 minutos de inatividade.
* **Código Organizado:** A lógica do bot está sendo feita de maneira modularizada utilizando o sistema de Cogs da biblioteca `discord.py`, separando as funcionalidades, facilitando a manutenção, expansão e leitura do código.

### 🤖 Comandos disponíveis
O prefixo para executar os comandos do bot é !
* !play <URL do youtube ou nome da música>
    * **Alternativa:** !p
    * **Descrição:** Busca a música pedida e a toca no seu canal de voz atual

* !leave
    * **Alternativa:** !l
    * **Descrição:** Desconecta o bot do canal de voz

### 🗺️ Planejamento de desenvolvimento futuro
* **Sistema de fila:** Adicionar um recurso de fila para a reprodução de músicas.
* **Controle de reprodução:** Implementar comandos de `!pause` e `!skip`.
* **Melhora na qualidade do áudio:** Pesquisar e implementar otimizações que reduzam o ruído.
* **Compatibilidade com o Spotify:** Estudar e implementar a API do Spotify para tocar playlists e músicas.
* **Rolagem de dados para RPG:** Adicionar comandos de rolagem de dados, como `!roll 2d20+5`, por exemplo, para jogos de RPG.