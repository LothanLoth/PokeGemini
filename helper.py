import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-2.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

def catch_pokemon(mensagem_usuario):
    try:
        validador = f"""
    1. Analyze the message provided by the user to identify the Pokémon they are looking for.
    2. Return only the name of the Pokémon, based on the original language and according to the PokeAPI.
    3. Do not add comments, emojis, explanations, line breaks, extra punctuation, or any other text beyond the identified Pokémon.

    Output format: only the Pokémon name in lowercase letters, without spaces or special characters.

    # Examples

    If the message is: "Who was Ash's first Pokémon?"
    Output: pikachu

    If the message is: "What is Squirtle's natural habitat?"
    Output: squirtle
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
        #Remove caracteres especiais e deixa minusculo
        return resposta.text.strip().lower()
      
    except:
        return "Could not locate this Pokémon"


