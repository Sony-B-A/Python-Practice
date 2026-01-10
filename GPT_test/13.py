# 🧪 TEST 2 — Dictionary + Function + Logic
marks = {
    "Sony": 78,
    "Preetham": 85,
    "Sangeeta": 88,
    "Aish": 92
}
 
def fxn(data):
    high_marks = max(data.values())
    for key in data:
        if(data.get(key) == high_marks):
            break
    return key, high_marks

name, score = fxn(marks)
tup = (name, score)
print(tup)