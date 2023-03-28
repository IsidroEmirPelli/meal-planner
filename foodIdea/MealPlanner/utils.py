import openai
import os
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def create_meal(ingredientes,custom_options):
    messages=[{"role": "system", "content": f"Esto son los ingredientes que tenemos: {ingredientes}"}]
    if custom_options is not None:
        messages += {"role": f"system", "content": f"Estos son ingredientes custom en caso de no contener alguna condicion alimenticia o un ingrediente ignoarlo: {custom_options}"}
    messages += [
        {"role": "system", "content": "Queremos hacer una comida que incluya o no los ingredientes, es para 1 persona, ignora todo lo que no sea comida o condiciones alimenticias"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        )
    return response['choices'][0]['message']
