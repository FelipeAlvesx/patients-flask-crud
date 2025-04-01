from flask import Flask, request, jsonify
from models.patients import Patient


app = Flask(__name__)
# CRUD
# get, post, delete, patch, put

patients = []
patient_id_control = 1


@app.route("/add-patient", methods=["POST"])
def add_patient():
    global patient_id_control
    data = request.get_json()
    test_git = True
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
        show_patient = [patient.name for patient in patients]
        print(show_patient)
        return jsonify({"message": "New Registered Patient", "id": new_patient.id})
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

    
@app.route("/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    data = request.get_json()
    patient = None
    for p in patients:
        if p.id == id:
            patient = p
            break
            
    if patient == None:
        return jsonify({"message": "Patient Not Foud"}), 404
    
    p.name = data["name"]
    p.age = data["age"]
    p.description = data["description"]
    p.room = data["room"]
    p.discharge = data["discharge"]

    return jsonify({"message": "Uptade success", "id": p.id})


@app.route("/patients/<int:id>", methods=["DELETE"])
def remove_patient(id):
    patient = None
    for p in patients:
        if p.id == id:
            patient = p
            break
    
    if not patient:
        return jsonify({"message": "Patient Not Found"}), 404

    patients.remove(patient)
    
    return jsonify({"message": "Patient Removed"})


if __name__ == "__main__":
    app.run(debug=True)
    