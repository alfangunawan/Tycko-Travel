from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import json
import os

app = Flask(__name__, template_folder='templates')

BOOKINGS_FILE = 'bookings.json'

# Daftar hotel di Indonesia
HOTELS = [
    {"name": "The Ritz-Carlton Jakarta", "city": "Jakarta", "price_range": "5000000-15000000"},
    {"name": "Four Seasons Hotel Jakarta", "city": "Jakarta", "price_range": "4000000-12000000"},
    {"name": "Mandarin Oriental Jakarta", "city": "Jakarta", "price_range": "3500000-10000000"},
    {"name": "The St. Regis Bali Resort", "city": "Bali", "price_range": "8000000-20000000"},
    {"name": "Four Seasons Resort Bali at Jimbaran Bay", "city": "Bali", "price_range": "7000000-18000000"},
    {"name": "The Mulia Bali", "city": "Bali", "price_range": "6000000-15000000"},
    {"name": "Padma Resort Ubud", "city": "Bali", "price_range": "3000000-8000000"},
    {"name": "Ayana Midplaza Jakarta", "city": "Jakarta", "price_range": "2500000-6000000"},
    {"name": "The Trans Resort Bali", "city": "Bali", "price_range": "2800000-7000000"},
    {"name": "Hotel Indonesia Kempinski Jakarta", "city": "Jakarta", "price_range": "3000000-8000000"}
]

def load_data():
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data():
    with open(BOOKINGS_FILE, 'w') as f:
        json.dump(bookings, f, indent=4)

bookings = load_data()

@app.route('/', methods=['GET'])
def booking_form():
    return render_template('booking_form.html', hotels=HOTELS)

@app.route('/bookings', methods=['POST'])
def create_booking():
    user = request.form.get('user')
    hotel = request.form.get('hotel')
    amount = request.form.get('amount')
    booking_id = f'B{len(bookings) + 1}'

    if not user or not hotel or not amount:
        return "Missing booking details", 400

    bookings[booking_id] = {
        'booking_id': booking_id,
        'user': user,
        'hotel': hotel,
        'amount': amount,
        'status': 'PENDING'
    }
    save_data()
    return redirect(url_for('payment_page', booking_id=booking_id))

@app.route('/pay/<booking_id>', methods=['GET', 'POST'])
def payment_page(booking_id):
    try:
        # Get booking data
        booking = bookings.get(booking_id)
        if not booking:
            return "Booking not found", 404

        # Payment methods and options
        payment_methods = ["credit", "debit", "e-wallet", "virtual-account"]
        payment_options = {
            "credit": ["BCA", "BNI", "Mandiri", "BRI", "CIMB", "Permata"],
            "debit": ["BCA", "BNI", "Mandiri", "BRI", "CIMB", "Permata"],
            "virtual-account": ["BCA", "BNI", "Mandiri", "BRI", "CIMB", "Permata"],
            "e-wallet": ["Gopay", "OVO", "DANA", "ShopeePay"]
        }

        if request.method == 'POST':
            payment_method = request.form.get('payment_method')
            bank = request.form.get('bank')

            if not payment_method or not bank:
                return "Metode pembayaran dan bank harus dipilih.", 400

            try:
                payment_response = requests.post(
                    'http://localhost:5002/payments',
                    json={
                        'booking_id': booking_id,
                        'amount': booking['amount'],
                        'payment_method': payment_method,
                        'bank': bank
                    }
                )
                result = payment_response.json()

                if payment_response.status_code == 200 and result.get('status') == 'PAID':
                    bookings[booking_id]['status'] = 'CONFIRMED'
                    save_data()
                    # return f"Pembayaran berhasil! Booking {booking_id} dikonfirmasi."
                    return redirect(url_for('payment_page', booking_id=booking_id))
                else:
                    bookings[booking_id]['status'] = 'FAILED'
                    save_data()
                    return f"Gagal memproses pembayaran. Status: {result.get('status')}"
            except Exception as e:
                return f"Terjadi error: {str(e)}", 500

        return render_template('payment_page.html', 
                            booking=booking, 
                            payment_methods=payment_methods,
                            payment_options=payment_options)
    except Exception as e:
        return str(e), 500

@app.route('/bookings', methods=['GET'])
def list_bookings():
    return jsonify(list(bookings.values())), 200

@app.route('/bookings/<booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = bookings.get(booking_id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404
    return jsonify(booking), 200

if __name__ == '__main__':
    app.run(port=5001)
