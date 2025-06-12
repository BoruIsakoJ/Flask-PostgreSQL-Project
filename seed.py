from models import *
from app import app


with app.app_context():
    
    Doctor.query.delete()
    Patient.query.delete()
    Appointment.query.delete()
    db.session.commit()
    
    doctor1 = Doctor(name="Ibrahim",specialization="Pyschologist")
    doctor2 = Doctor(name="Frank",specialization="Pediatricians")
    doctor3 = Doctor(name="Boru",specialization="Cardiologist")
    
    
    patient1 = Patient(name="Moriaso")
    patient2 = Patient(name="Elijah")
    patient3 = Patient(name="Hagee")
    patient4 = Patient(name="Fahiye")
    patient5 = Patient(name="Kiptoo")
    
    appointment1 = Appointment(doctor_id =1, patient_id=1)
    appointment2 = Appointment(doctor_id =2, patient_id=2)
    appointment3 = Appointment(doctor_id =3, patient_id=3)
    appointment4 = Appointment(doctor_id =1, patient_id=4)
    appointment5 = Appointment(doctor_id =2, patient_id=5)
    
    db.session.add_all([doctor1,doctor2,doctor3,patient1,patient2,patient3,patient4,patient5,appointment1,appointment2,appointment3,appointment4,appointment5])
    db.session.commit()
    
