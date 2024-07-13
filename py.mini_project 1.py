class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender}"


class Patient(Person):
    def __init__(self, name, age, gender, patient_id):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.medical_records = []

    def add_medical_record(self, record):
        self.medical_records.append(record)

    def display_medical_record(self):
        print("Medical records for", self.name)
        for record in self.medical_records:
            print(record)


class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def display_appointments(self):
        print("Appointments for Dr.", self.name)
        for appointment in self.appointments:
            print(appointment)


class Appointment:
    def __init__(self, appointment_id, doctor, patient, date, time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def display_info(self):
        print(f"Appointment ID: {self.appointment_id} \nDoctor: {self.doctor.name} \nPatient: {self.patient.name} \nDate: {self.date} \nTime: {self.time}")


class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"{patient.name} added to the hospital")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"{doctor.name} added to the hospital")

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        appointment.doctor.add_appointment(appointment)
        appointment.patient.add_medical_record(f"Appointment on {appointment.date} at {appointment.time} with Dr. {appointment.doctor.name}")
        print(f"Scheduled appointment {appointment.appointment_id}")

    def display_patients(self):
        print("Patients in the hospital:")
        for patient in self.patients:
            print(patient)

    def display_doctors(self):
        print("Doctors in the hospital:")
        for doctor in self.doctors:
            print(doctor)

    def display_appointments(self):
        print("Appointments in the hospital:")
        for appointment in self.appointments:
            appointment.display_info()


class Address:
    def __init__(self, city, state, pin):
        self.city = city
        self.state = state
        self.pin = pin

    def __str__(self):
        return f"{self.city}, {self.state}, {self.pin}"


address = Address("Kolkata", "West Bengal", 700001)
hospital = Hospital("ABC Hospital", address)

doctor1 = Doctor("Dr. Mukherjee", 35, "Male", "DOC123", "Cardiology")
hospital.add_doctor(doctor1)

patient1 = Patient("mr.Bose", 30, "Male", "PAT123")
hospital.add_patient(patient1)

appointment1 = Appointment("APP123", doctor1, patient1, "2023-05-15", "10:00 AM")
hospital.add_appointment(appointment1)

hospital.display_patients()
hospital.display_doctors()
hospital.display_appointments()

doctor1.display_appointments()
patient1.display_medical_record()

