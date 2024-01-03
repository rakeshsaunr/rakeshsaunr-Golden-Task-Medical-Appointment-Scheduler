from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory data storage (Replace this with a database in a production environment)
appointments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    data = request.json

    # Validate data (you can add more validations)
    if 'patient_name' not in data or 'doctor_name' not in data or 'date_time' not in data:
        return jsonify({'error': 'Incomplete data'}), 400

    # Save appointment
    appointment = {
        'patient_name': data['patient_name'],
        'doctor_name': data['doctor_name'],
        'date_time': data['date_time']
    }
    appointments.append(appointment)

    return jsonify({'message': 'Appointment scheduled successfully'})

@app.route('/get_appointments')
def get_appointments():
    return jsonify({'appointments': appointments})

if __name__ == '__main__':
    app.run(debug=True)
