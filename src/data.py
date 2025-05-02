# Embedded Doctor Data
DOCTOR_DATA = {
    "doctor_name": [
        "Dr. John Smith",
        "Dr. Emily Davis",
        "Dr. Michael Brown",
        "Dr. Sarah Johnson",
        "Dr. Daniel Lee",
        "Dr. Olivia Martinez",
        "Dr. William Garcia",
        "Dr. Ava Wilson",
        "Dr. James White",
        "Dr. Sophia Taylor"
    ],
    "specialty": [
        "Cardiologist",
        "Dermatologist",
        "Orthopedic",
        "Pediatrician",
        "Neurologist",
        "Ophthalmologist",
        "ENT Specialist",
        "Psychiatrist",
        "Endocrinologist",
        "Gastroenterologist"
    ],
    "available_timings": [
        "10:00 AM - 1:00 PM",
        "2:00 PM - 5:00 PM",
        "9:00 AM - 12:00 PM",
        "1:00 PM - 4:00 PM",
        "11:00 AM - 2:00 PM",
        "3:00 PM - 6:00 PM",
        "8:00 AM - 11:00 AM",
        "1:00 PM - 3:00 PM",
        "10:00 AM - 12:00 PM",
        "2:00 PM - 4:00 PM"
    ]
}

# Symptom-to-Condition Mapping (CSP-based)
symptom_conditions = {
    "Flu": {"required": {"fever", "cough"}, "optional": {"sore throat", "fatigue"}},
    "Migraine": {"required": {"headache", "dizziness"}, "optional": {"nausea", "sensitivity to light"}},
    "Strep Throat": {"required": {"sore throat", "fever"}, "optional": {"swollen glands", "rash"}},
    "Asthma": {"required": {"cough", "shortness of breath"}, "optional": {"wheezing", "chest tightness"}},
    "Measles": {"required": {"fever", "rash"}, "optional": {"cough", "red eyes"}},
    "Food Poisoning": {"required": {"nausea", "vomiting"}, "optional": {"diarrhea", "abdominal pain"}},
}