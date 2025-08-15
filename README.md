title: "PokeGemini 🐾⚡"
cover_image: "https://github.com/user-attachments/assets/5bdc42de-e5fd-4200-bb8d-e001cc5166f7"
badges:
  - "https://img.shields.io/github/license/seu-usuario/pokegemini"
  - "https://img.shields.io/badge/Python-3.x-blue"
  - "https://img.shields.io/badge/Flask-2.x-lightgrey"
  - "https://img.shields.io/badge/status-em%20desenvolvimento-yellow"
description: |
  Um chatbot multimodal inspirado no universo Pokémon, desenvolvido com Flask, Google Gemini API e PokeAPI.
  Ele interpreta mensagens, identifica o Pokémon mencionado, adapta seu tom de resposta conforme o sentimento do usuário
  e mantém a conversa imersiva como se fosse o próprio Professor Carvalho.
features:
  - "Personas dinâmicas: muda o tom de resposta conforme o sentimento detectado (positivo, neutro ou negativo)"
  - "Integração com PokeAPI: busca dados reais de Pokémon (altura, peso, tipo, habilidades)"
  - "Suporte a imagens: permite enviar imagens para análise e respostas mais ricas"
  - "Histórico de conversa: mantém contexto e coerência ao longo do diálogo"
  - "Formato narrativo: sem Markdown ou HTML, aumentando a imersão"
technologies:
  - "Python 3"
  - "Flask"
  - "Google Generative AI - Gemini"
  - "PokeAPI"
  - "Python-dotenv"
  - "HTML, CSS e JavaScript"
project_structure: |
  📦 PokeGemini
  ┣ 📂 static
  ┃ ┣ 📂 css
  ┃ ┣ 📂 img
  ┃ ┗ 📂 js
  ┣ 📂 templates
  ┃ ┗ index.html
  ┣ 📜 app.py
  ┣ 📜 helper.py
  ┣ 📜 persona_select.py
  ┣ 📜 cache.py
  ┣ 📜 gerenciar_imagem.py
  ┣ 📜 .env.example
  ┗ 📜 README.md
setup_instructions:
  - step: "Clone o repositório"
    command: |
      git clone https://github.com/seu-usuario/pokegemini.git
      cd pokegemini
  - step: "Crie e ative o ambiente virtual"
    command: |
      python -m venv venv
      # Windows
      venv\Scripts\activate
      # Linux/Mac
      source venv/bin/activate
  - step: "Instale as dependências"
    command: |
      pip install -r requirements.txt
  - step: "Configure as variáveis de ambiente"
    command: |
      Crie um arquivo `.env` na raiz do projeto:
      GEMINI_API_KEY=SUA_CHAVE_AQUI
  - step: "Execute o servidor"
    command: |
      python app.py
  - step: "Acesse no navegador"
    command: |
      http://127.0.0.1:5000
demo_section:
  description: "Adicione aqui um print ou GIF mostrando o chatbot em funcionamento"
  example_image: "static/img/demo.png"
license:
  text: "Este projeto é de uso livre para fins educacionais e de portfólio"
