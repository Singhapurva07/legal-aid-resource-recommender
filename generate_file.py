import pandas as pd
import random

states = ["Uttar Pradesh", "Maharashtra", "Bihar", "West Bengal", "Madhya Pradesh",
          "Tamil Nadu", "Rajasthan", "Karnataka", "Gujarat", "Andhra Pradesh",
          "Odisha", "Telangana", "Kerala", "Jharkhand", "Assam", "Punjab",
          "Chhattisgarh", "Haryana", "Delhi", "Jammu & Kashmir"]

cities = {
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur"],
    "West Bengal": ["Kolkata", "Howrah", "Siliguri"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
    "Karnataka": ["Bengaluru", "Mysore", "Mangalore"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Andhra Pradesh": ["Vijayawada", "Visakhapatnam", "Guntur"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
    "Kerala": ["Kochi", "Thiruvananthapuram", "Kozhikode"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh"],
    "Punjab": ["Ludhiana", "Amritsar", "Chandigarh"],
    "Chhattisgarh": ["Raipur", "Bilaspur", "Durg"],
    "Haryana": ["Gurgaon", "Faridabad", "Panipat"],
    "Delhi": ["New Delhi"],
    "Jammu & Kashmir": ["Srinagar", "Jammu"]
}

case_types = ["Domestic Violence", "Property Dispute", "Sexual Harassment", "Dowry", 
              "Child Abuse", "Cyber Crime", "Senior Citizen Abuse", "Caste Discrimination"]

resource_types = ["Legal Aid NGO", "District Legal Services Authority", "Legal Clinic", 
                  "Women's Helpline", "Cyber Helpline", "Childline", "Elder Help NGO"]

def generate_entry():
    state = random.choice(states)
    city = random.choice(cities[state])
    case_type = random.choice(case_types)
    resource_type = random.choice(resource_types)
    resource_name = f"{resource_type} - {city} {random.randint(1, 99)}"
    contact = f"+91-{random.randint(7000000000, 9999999999)}"
    return {
        "State": state,
        "City": city,
        "Case_Type": case_type,
        "Resource_Name": resource_name,
        "Resource_Type": resource_type,
        "Contact": contact
    }

entries = [generate_entry() for _ in range(1000)]
df = pd.DataFrame(entries)
df.to_csv("legal_aid_resources_1000.csv", index=False)
