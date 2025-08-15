from flask import Flask,render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests
from time import sleep
from helper import catch_pokemon
from persona_select import personas, selecionar_persona
from cache import remover_mensagens_antigas
import uuid 
from gerenciar_imagem import gerar_imagem_gemini

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-2.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

app = Flask(__name__)

caminho_imagem_enviada = None
UPLOAD_FOLDER = "imagens_temporarias"

def criar_chatbot():

    prompt_do_sistema = f"""
        # PERSONA

        You are Professor Oak, the renowned Pokémon researcher from Kanto.
        Your personality is wise, patient, and curious, with a touch of gentle humor.
        You always encourage new trainers, tell stories from the Pokémon world, and explain
        concepts in a detailed and educational way.

        Role-playing guidelines:
        - Always speak as if you are in a Pokémon lab or on an adventure.
        - Use iconic expressions like “Hmm…” or “Ah, yes!” to bring your responses to life.
        - When explaining something about a Pokémon, include details such as height, weight, types, abilities, and fun facts.
        - Always encourage the user as if guiding a new trainer on their journey.
        - If the user asks about a Pokémon, use real data (e.g., from PokeAPI) and present it narratively.
        - When you dont know something, invent a response consistent with the Pokémon universe.
        - Keep a friendly, teacher-like, and immersive tone, as if the user were inside the Pokémon world.

        ### FORMATTING RULES
        - Do not use bold, italics, underline, numbered lists, or bullet points.
        - Do not use Markdown (`**`, `_`, etc.) or HTML (`<b>`, `<i>`, etc.).
        - Produce only plain text with normal punctuation.
        - Line breaks only when necessary to separate paragraphs.

        Example response:
        "
            "Ah, yes! Pikachu, the famous Electric Mouse Pokémon. It measures about 40 centimeters and weighs 6 kilograms.

            "
            name:
            height:
            weight:
            type:
            "

            Its body stores electricity, and when excited, its cheeks release sparks!
            An excellent companion for beginner trainers… as long as you are ready for a few shocks!"
        "

        # PERSONALITY
        {personas}

        # HISTORY
        Always access the message history and retrieve information previously mentioned.
    """


    configuracao_modelo = {
        "temperature" : 1.0,
        "max_output_tokens" : 8192
    }

    llm = genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt_do_sistema,
        generation_config=configuracao_modelo
    )

    chatbot = llm.start_chat(history=[])

    return chatbot

chatbot = criar_chatbot()



def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    global caminho_imagem_enviada
    while True:
        try:


            url = f"https://pokeapi.co/api/v2/pokemon/{catch_pokemon(prompt)}"

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
            else:
                data = 'Não foi encontrara uma pagina especifica no PokeApi. Prossiga para próxima parte'

            personalidade = personas[selecionar_persona(prompt)]

            mensagem_usuario = f"""
            consider this personality when responding to messages: {personalidade}

            Respond to the following message while always keeping the history in mind:
            {prompt}


            # CONTEXT
            Use the information provided in the context below to answer the questions:
            {data}
            """


            if caminho_imagem_enviada:
                mensagem_usuario += '\n use the characteristics of the image in your response'
                arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
                resposta = chatbot.send_message([arquivo_imagem, mensagem_usuario])
                os.remove(caminho_imagem_enviada)
                caminho_imagem_enviada = None
            else:
                resposta = chatbot.send_message(mensagem_usuario)



            if len(chatbot.history) > 10:
                chatbot.history = remover_mensagens_antigas(chatbot.history)
            return resposta.text

        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            
            if caminho_imagem_enviada:
                os.remove(caminho_imagem_enviada)
                caminho_imagem_enviada=None

            sleep(50)

@app.route("/upload_imagem", methods=['POST'])
def upload_imagem():
    global caminho_imagem_enviada

    if "imagem" in request.files:
        imagem_enviada = request.files["imagem"]
        nome_do_arquivo = str(uuid.uuid4()) + os.path.splitext(imagem_enviada.filename)[1]
        caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_do_arquivo)
        imagem_enviada.save(caminho_arquivo)
        caminho_imagem_enviada = caminho_arquivo
        return "Imagem enviada com sucesso", 200
    return"Nenhum arquivo enviado",400

@app.route("/chat", methods=['POST'])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta



@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
