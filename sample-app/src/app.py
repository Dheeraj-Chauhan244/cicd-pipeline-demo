from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'CI/CD Pipeline Demo',
        'version': '1.0.0',
        'environment': os.environ.get('ENV', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/test')
def test():
    return jsonify({'message': 'Pipeline test successful!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)