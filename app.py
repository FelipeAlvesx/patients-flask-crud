from flask import Flask, request, jsonify
from models.patients import Patient


app = Flask(__name__)
# CRUD

patients = []
patient_id_control = 1


@app.route("/add-patient", methods=["POST"])
def add_patient():
    global patient_id_control
    data = request.get_json()
    try:
        new_patient = Patient(
            id=patient_id_control,
            name=data["name"],
            age=data["age"],
            description=data["description"],
            room=data["room"],
           # discharge=["discharge"]
        )
        patient_id_control += 1
        patients.append(new_patient)
        print(patients)
        return jsonify({"message": "New Registered Patient"})
    except:
        return "Error Something is Wrong"


@app.route("/patients", methods=["GET"])
def get_all_patients():
        patient_list = [patient.to_dict() for patient in patients]
        print(patient_list)
        
        output = {
            "patients": patient_list,
            "total_patients": len(patient_list)
        }
        
        return jsonify(output)


@app.route("/patients/<int:id>", methods=["GET"])
def get_pacient(id):
    for patient in patients:
        if patient.id == id:
            return jsonify(patient.to_dict())
    
    return jsonify({"message": "Not Found"}), 404
    
    
if __name__ == "__main__":
    app.run(debug=True)
    