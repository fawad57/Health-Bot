from data import DOCTOR_DATA

def format_doctor_data():
    """Format all doctor data for display."""
    result = []
    for name, specialty, timing in zip(DOCTOR_DATA["doctor_name"], DOCTOR_DATA["specialty"], DOCTOR_DATA["available_timings"]):
        result.append(f"{name}, {specialty}, Available: {timing}")
    return "\n".join(result)

def filter_doctors_by_specialty(specialty):
    """Filter doctors by their specialty."""
    result = []
    for name, spec, timing in zip(DOCTOR_DATA["doctor_name"], DOCTOR_DATA["specialty"], DOCTOR_DATA["available_timings"]):
        if specialty.lower() in spec.lower():
            result.append(f"{name}, {spec}, Available: {timing}")
    return "\n".join(result) if result else f"No doctors found for the specialty '{specialty}'."