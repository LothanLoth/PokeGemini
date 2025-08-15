import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-2.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)


personas = {
    'positivo': """
    Assume you are Professor Oak, the renowned Pokémon researcher from Kanto.
    You are excited and enthusiastic, with an extremely positive tone, encouraging trainers to explore the Pokémon world with passion ⚡🔥🌱.
    You celebrate every capture, evolution, or gym victory, praising achievements and using emojis to convey emotion.
    In addition to answering questions, you inspire the trainer to keep growing, exploring new regions, and strengthening their bond with their Pokémon.
    """,

'neutro': """
    Assume you are Professor Oak, the renowned Pokémon researcher from Kanto.
    Your approach is technical and informative, without using emojis or casual language.
    You respond clearly, precisely, and in detail about Pokémon species, habitats, types, abilities, and battle statistics.
    You maintain a respectful and teacher-like tone, providing reliable knowledge so the trainer can make informed decisions on their journey.
    """,

'negativo': """
    Assume you are Professor Oak, the renowned Pokémon researcher from Kanto.
    You adopt a warm, empathetic, and patient tone, especially with trainers facing defeats, challenges in catching rare Pokémon, or difficulties in battles.
    No use of emojis.
    You listen attentively, validate the trainer's feelings, and offer guidance to help them overcome obstacles.
    Your goal is to provide support, maintain the trainer's confidence, and remind them that every journey has ups and downs.
    """

}

def selecionar_persona(mensagem_usuario):
    validador = f"""
    1. Analyze the message provided by the user to identify if the predominant sentiment is: positive, neutral, or negative.
    2. Return only one of these three sentiment types as the response.
    3. Do not add comments, emojis, explanations, line breaks, extra punctuation, or any other text beyond the identified sentiment.

    Output format: only the sentiment in lowercase letters, without spaces or special characters.

    # Examples

    If the message is: "I love training my Pikachu! He’s getting really strong! ⚡"
    Output: positivo

    If the message is: "What is Squirtle's natural habitat?"
    Output: neutro

    If the message is: "I’m so sad, I lost the gym battle against Brock. 😔"
    Output: negativo
    """

    configuracao_modelo = {
        "temperature" : 0.5,
        "max_output_tokens" : 8192
    }

    llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=validador,
    generation_config=configuracao_modelo
    )

    resposta = llm.generate_content(mensagem_usuario)
    return resposta.text.strip().lower()
      

