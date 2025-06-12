from flask import Flask
from sqlalchemy import MetaData,DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
import datetime



metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'
    
    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String, nullable=False)
    created_at=db.Column(db.DateTime, default =datetime.datetime.now())
    
    appointments = db.relationship("Appointment", back_populates='patient')
    serialize_rules = ('-appointments.patient',)

    

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'
    
    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String, nullable=False)
    specialization =db.Column(db.String)
    created_at=db.Column(db.DateTime, default =datetime.datetime.now())
    
    appointments = db.relationship("Appointment", back_populates='doctor')
    serialize_rules = ('-appointments.doctor',)

    
class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'
    
    id =db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    
    created_at=db.Column(db.DateTime, default =datetime.datetime.now())
    
    patient = db.relationship('Patient', back_populates='appointments')
    doctor = db.relationship('Doctor', back_populates='appointments')
    
    serialize_rules = ('-patient.appointments','-doctor.appointments',)