from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__, template_folder='templates')

PAYMENTS_FILE = 'payments.json'

def load_data():
    if os.path.exists(PAYMENTS_FILE):
        with open(PAYMENTS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data():
    with open(PAYMENTS_FILE, 'w') as f:
        json.dump(payments, f, indent=4)

payments = load_data()

@app.route('/')
def home():
    return render_template('payment_list.html', payments=list(payments.values()))

@app.route('/payments', methods=['POST'])
def process_payment():
    data = request.get_json()
    booking_id = data.get('booking_id')
    amount = data.get('amount')
    payment_method = data.get('payment_method')  # credit/debit
    bank = data.get('bank')  # nama bank

    if not booking_id or not amount or not payment_method or not bank:
        return jsonify({'message': 'Invalid payment request', 'status': 'FAILED'}), 400

    payments[booking_id] = {
        'booking_id': booking_id,
        'amount': amount,
        'payment_method': payment_method,
        'bank': bank,
        'status': 'PAID'
    }
    save_data()
    return jsonify({'message': 'Payment successful', 'status': 'PAID'}), 200


@app.route('/payments', methods=['GET'])
def list_payments():
    # Check if the request wants JSON
    if request.headers.get('Accept') == 'application/json':
        return jsonify(list(payments.values())), 200
    # Otherwise return HTML
    return render_template('payment_list.html', payments=list(payments.values()))


@app.route('/payments/<booking_id>', methods=['GET'])
def get_payment(booking_id):
    payment = payments.get(booking_id)
    if not payment:
        return jsonify({'error': 'Not found'}), 404
    
    # Check if the request wants JSON
    if request.headers.get('Accept') == 'application/json':
        return jsonify(payment), 200
    # Otherwise return HTML
    return render_template('payment_detail.html', payment=payment)

@app.route('/payment-methods', methods=['GET'])
def get_payment_methods():
    methods = ["credit", "debit", "e-wallet", "virtual-account"]
    return jsonify(methods), 200

@app.route('/banks', methods=['GET'])
def get_banks():
    payment_method = request.args.get('method')
    
    if payment_method == 'e-wallet':
        payment_options = ["Gopay", "OVO", "DANA", "ShopeePay"]
    else:
        payment_options = ["BCA", "BNI", "Mandiri", "BRI", "CIMB", "Permata"]
    
    return jsonify(payment_options), 200

if __name__ == '__main__':
    app.run(port=5002)
