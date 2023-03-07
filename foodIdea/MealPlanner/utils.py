import openai
import os
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

def create_meal(ingredientes):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"Estos son los ingredientes que tenemos: {ingredientes}"},
                {"role": "system", "content": "Queremos hacer una comida que incluya o no los ingredientes, es para 1 persona, ignora todo lo que no sea comida"},
                {"role": "system", "content": "Esta respuesta va a estar dentro de un <p> En caso de tener receta dame los pasos de la receta separados usando <br>"},
            ]
        )
    return response['choices'][0]['message']
