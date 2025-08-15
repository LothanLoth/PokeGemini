# PokeGemini 🐾⚡
# Description: |
  PokeGemini is a multimodal chatbot inspired by the Pokémon universe, developed with Flask, Google Gemini API, and PokeAPI.
  It interprets messages, identifies the mentioned Pokémon, adapts its response tone according to the user's sentiment,
  and keeps the conversation immersive as if it were Professor Oak himself.
# Features:
  - "Dynamic personas: changes response tone according to detected sentiment (positive, neutral, or negative)"
  - "PokeAPI integration: fetches real Pokémon data (height, weight, type, abilities)"
  - "Image support: allows sending images for analysis and richer responses"
  - "Conversation history: maintains context and coherence throughout the dialogue"
  - "Narrative format: no Markdown or HTML, enhancing immersion"
# Technologies:
  - "Python 3"
  - "Flask"
  - "Google Generative AI - Gemini"
  - "PokeAPI"
  - "Python-dotenv"
  - "HTML, CSS, and JavaScript"
# Project_structure: |
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
# Setup_instructions:
  - step: "Clone the repository"
    command: |
      git clone https://github.com/your-username/pokegemini.git
      cd pokegemini
  - step: "Create and activate the virtual environment"
    command: |
      python -m venv venv
      # Windows
      venv\Scripts\activate
      # Linux/Mac
      source venv/bin/activate
  - step: "Install dependencies"
    command: |
      pip install -r requirements.txt
  - step: "Set up environment variables"
    command: |
      Create a `.env` file in the project root:
      GEMINI_API_KEY=YOUR_KEY_HERE
  - step: "Run the server"
    command: |
      python app.py
  - step: "Access in the browser"
    command: |
      http://127.0.0.1:5000
