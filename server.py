from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# In-memory data
data = {
    'users': [{'id': 1, 'email': 'user@example.com', 'balance': 1250.75, 'status': 'active'}],
    'deposits': [],
    'withdrawals': [],
    'plans': [
        {'id': 1, 'name': 'Starter', 'min': 100, 'max': 1000, 'duration': '7 days', 'profit': '15%'},
        {'id': 2, 'name': 'Silver', 'min': 1000, 'max': 5000, 'duration': '14 days', 'profit': '25%'},
        {'id': 3, 'name': 'Gold', 'min': 5000, 'max': 20000, 'duration': '30 days', 'profit': '40%'},
        {'id': 4, 'name': 'VIP', 'min': 20000, 'max': 100000, 'duration': '60 days', 'profit': '60%'}
    ],
    'transactions': []
}

ADMIN_USER = 'makeit001'
ADMIN_PASS = 'Makemoney@12'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

@app.route('/api/login', methods=['POST'])
def login():
    return jsonify({'success': True, 'user': {'email': request.json.get('email'), 'balance': 1250.75}})

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    if data.get('username') == ADMIN_USER and data.get('password') == ADMIN_PASS:
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data['users'])

@app.route('/api/deposits', methods=['GET'])
def get_deposits():
    return jsonify(data['deposits'])

@app.route('/api/withdrawals', methods=['GET'])
def get_withdrawals():
    return jsonify(data['withdrawals'])

@app.route('/api/plans', methods=['GET'])
def get_plans():
    return jsonify(data['plans'])

@app.route('/api/deposits/approve/<int:dep_id>', methods=['POST'])
def approve_deposit(dep_id):
    for dep in data['deposits']:
        if dep.get('id') == dep_id:
            user = next((u for u in data['users'] if u['id'] == dep.get('userId')), None)
            if user:
                user['balance'] += dep.get('amount', 0)
            dep['status'] = 'approved'
            data['transactions'].append({'type': 'deposit', **dep})
            return jsonify({'success': True})
    return jsonify({'success': False}), 404

@app.route('/api/balance/update', methods=['POST'])
def update_balance():
    req = request.json
    user = next((u for u in data['users'] if u['id'] == req.get('userId')), None)
    if user:
        user['balance'] += float(req.get('amount', 0))
        return jsonify({'success': True, 'newBalance': user['balance']})
    return jsonify({'success': False}), 404

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    return jsonify(data['transactions'])

if __name__ == '__main__':
    print("🚀 CryptoEarner Server running!")
    print("Visit http://localhost:5000")
    print("Admin: makeit001 / Makemoney@12")
    app.run(debug=True, port=5000)
