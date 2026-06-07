from flask import Flask, render_template, request, jsonify
from designer_agent import designer_agent
from coder_agent import coder_agent
from playtester_agent import playtester_agent
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    game_idea = request.json['idea']
    
    # Agent 1
    spec = designer_agent(game_idea)
    time.sleep(60)
    
    # Agent 2
    code = coder_agent(spec)
    time.sleep(60)
    
    # Agent 3
    review = playtester_agent(spec, code)
    
    return jsonify({
        'spec': spec,
        'review': review
    })

if __name__ == '__main__':
    app.run(debug=False)