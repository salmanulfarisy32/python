#convert two lists into a dictionary
keys=['ten','twenty','thirty']
values=[10,20,30]
result=dict(zip(keys,values))
print(result)
#merge two python dictionaries into one
dict1={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'fourty':40}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)
#print the value of key 'history' from the dict
sampledict={
    "class":{
        "student":{
            "name":"mike",
            "mark":{
                "physics":70,
                "history":80
            }
        }
    }
}
print(sampledict['class']['student']['mark']['history'])
#initialize dictionary with dafault values
employees=['kelly','emma']
defaults={"designation":'developer',"salary":8000}
res=dict.fromkeys(employees,defaults)
print(res)
print(res["kelly"])
