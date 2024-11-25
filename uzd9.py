from transformers import pipeline

def generate_text(prompt):
    gen = pipeline('text-generation', model='gpt2')
    result = gen(prompt, max_length=100, num_return_sequences=1)
    print(f"Generated text:\n{result[0]['generated_text']}")
    return result[0]['generated_text']
