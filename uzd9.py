from transformers import pipeline

def teksta_generesana(sakums):
    
    generator = pipeline('text-generation', model='gpt2')
    
    rezultats = generator(sakums, max_length=100, num_return_sequences=1)
    
    print("Ģenerētais teksts:")
    print(rezultats[0]['generated_text'])
    
    return rezultats[0]['generated_text']