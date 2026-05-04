import csv
def load_csv(filename):
    with open(filename, "r", newline='') as fr:
        reader = csv.DictReader(fr)
        return list(reader)
    
def save_csv(filename, data):
    if len(data) == 0:
        return 
    fieldnames = list(data[0].keys())
    with open(filename,"w",newline='') as fw:
        writer = csv.DictWriter(fw, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

        
        
    
