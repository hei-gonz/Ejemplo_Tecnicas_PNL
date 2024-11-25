
from transformers import AutoTokenizer, AutoModelForCausalLM

# Cargar el modelo y el tokenizador
model_name = "meta-llama/Llama-2-7b-hf"  # Ejemplo con el modelo de Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Crear un prompt y generar texto
prompt = "Explícame qué es LLaMA-2 en lenguaje sencillo:"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")  # Enviar a GPU si está disponible
outputs = model.generate(**inputs, max_new_tokens=50)

# Decodificar la respuesta
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
