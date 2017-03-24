# Complete the function below.

class Doctor():
    
    def __init__(self, id, name, zip, scripts_per_week_avg, script_avg_val):
        self.id = id
        self.name = name
        self.zip = zip
        self.scripts_per_week_avg = scripts_per_week_avg
        self.script_avg_val = script_avg_val
    
    def get_items(self):
        return [self.id,
                self.name,
                self.zip,
                self.scripts_per_week_avg,
                self.script_avg_val]  
    
    def __str__(self):
        
        items = self.get_items()
        items = map(str, items)
        return ",".join(items)
    
    @classmethod
    def from_csv_str(cls, csv_str):
        items = csv_str.split(",")
        
        id = int(items[0])
        name = items[1]
        zip = int(items[2])
        scripts_per_week_avg = float(items[3])
        script_avg_val = float(items[4])
        
        return cls(id, name, zip, scripts_per_week_avg, script_avg_val)
        

def doctor_sort(csv_string):
    
    csv_strs = csv_string.split("\n")
    
    doctors = []
    
    for csv_str in csv_strs:
        doctor = Doctor.from_csv_str(csv_str)
        doctors.append(doctor)
    
    doctors.sort(key = lambda doctor : (doctor.scripts_per_week_avg, -1*doctor.script_avg_val))
    
    doctors = map(str, doctors)
    
    doctors = "\n".join(doctors)
    
    return doctors

csv = """1,alex,80405,13,5
3,bob,94123,320,1.5
2,jane,94032,35,2.8
4,will,94110,31.6,6.1
5,jess,94117,48,4
6,sam,94032,31.4,9
7,jim,94036,35,19"""

print(doctor_sort(csv))