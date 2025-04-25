# Travel Agent Booking System

A modern microservices-based hotel booking system that allows users to book luxury hotels across Indonesia and process payments seamlessly.

## 🌟 Features

- Browse premium hotels across Indonesia
- Easy booking process
- Multiple payment methods support
- Real-time booking status tracking
- Secure payment processing

## 🏗️ Architecture

The system consists of two microservices:

1. **Booking Service** (Port 5001)
   - Manages hotel listings
   - Handles booking creation
   - Tracks booking status
   - Provides booking management interface

2. **Payment Service** (Port 5002)
   - Processes payments
   - Supports multiple payment methods
   - Manages payment status
   - Provides payment history

## 🏨 Available Hotels

Premium hotels available in the system include:
- The Ritz-Carlton Jakarta
- Four Seasons Hotel Jakarta
- Mandarin Oriental Jakarta
- The St. Regis Bali Resort
- Four Seasons Resort Bali
- The Mulia Bali
- And more...

## 💳 Payment Options

The system supports various payment methods:
- Credit Card
- Debit Card
- E-Wallet (Gopay, OVO, DANA, ShopeePay)
- Virtual Account

Supported Banks:
- BCA
- BNI
- Mandiri
- BRI
- CIMB
- Permata

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Web browser (Chrome, Firefox, or Safari recommended)

### Installation Steps

1. Clone the repository or download the project files:
```bash
git clone <your-repository-url>
cd travel-agent-project
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install flask requests
```

### Running the Application

1. Start the Payment Service first:
```bash
cd payment_service
python payment_service.py
```
The service will run on http://localhost:5002

2. Open a new terminal and start the Booking Service:
```bash
cd booking_service
python booking_service.py
```
The service will run on http://localhost:5001
