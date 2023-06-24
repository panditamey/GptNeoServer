from flask import Flask, jsonify, request
from transformers import pipeline
app = Flask(__name__)
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
@app.route('/', methods = ['GET', 'POST'])
def home():
    
    if(request.method == 'GET'):
  
        info = "gpt neo server"
        return jsonify({'info': info})
    if(request.method == 'POST'):
        jsonData = request.get_json()
        # print(prompt['prompt'])
        # prompt = "India is "
        prompt = jsonData['prompt']
        res = generator(prompt, max_length=200, do_sample=True, temperature=0.9) 
        return jsonify({'data': res[0]['generated_text']})
    
if __name__ == '__main__':
  
    app.run(debug = True)