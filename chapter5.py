#dictonery
match={} #empty dict
marks= {"aayush":98,
        "vijay": 88,
        "hard":89,}
print(marks)
print(type(marks))
print(marks["aayush"])
#methods
marks= {"aayush":98,
        "vijay": 88,
        "hard":89,}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"aayush":99,"soft": 55})
print(marks)
print(marks.get("aayush"))
print(marks.get("aayussh")) #prints none
# print(marks["aayussh"]) #prints error
print(marks.clear())
newmarks = marks.copy()
print(new nmarks)

