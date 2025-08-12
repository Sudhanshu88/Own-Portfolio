from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv  # Correct absolute import

# Load environment variables from .env file
load_dotenv()

# Optional: If you want to disable Flask's built-in dotenv loader
# (usually unnecessary if you manage dotenv manually)
os.environ['FLASK_SKIP_DOTENV'] = '1'

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Serve the homepage
@app.route('/')
def serve_index():
    return render_template('index.html')

# Contact form API endpoint
@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json(force=True)
    if not data:
        return jsonify({'error': 'Invalid request format'}), 400

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'All fields are required'}), 400

    # Log received data - replace with database or email integration as needed
    print('New contact form submission:', {
        'name': name,
        'email': email,
        'message': message
    })

    return jsonify({'message': 'Thank you for reaching out! I will get back to you soon.'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)
