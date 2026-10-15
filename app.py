from flask_cors import CORS
CORS(app, origins=["https://elaborate-profiterole-a2ede4.netlify.app", "*"])
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "MedScribe API Running", "version": "MVP 1.0"})

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    # Phase 1: Browser Web Speech API
    # Phase 2: Whisper on-device + Bhashini API
    data = request.json
    hindi_text = data.get('text', '')
    return jsonify({
        "transcribed_text": hindi_text,
        "translated": hindi_text, # Bhashini integration in Phase 2
        "language": "hi-IN"
    })

@app.route('/api/generate-prescription', methods=['POST'])
def generate_prescription():
    # Phase 2: GPT-4 / Llama will parse symptoms -> prescription
    symptoms = request.json.get('symptoms', '')
    prescription = {
        "patient_complaint": symptoms,
        "diagnosis": "Fever + Cold (AI Suggested)",
        "medicines": ["Paracetamol 500mg", "Cetirizine"],
        "advice": "Rest and hydration"
    }
    return jsonify(prescription)

if __name__ == '__main__':
    app.run(debug=True)