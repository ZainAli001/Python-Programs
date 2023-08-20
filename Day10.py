import json
# Exercise 1: Convert the following dictionary into JSON format
data = {"key1": "value1", "key2": "value2"}
json_data = json.dumps(data)
print(type(json_data))

# -------------------------------------------------------
# Exercise 2: Access the value of key2 from the following JSON

sampleJson = """{"key1": "value1", "key2": "value2"}"""
# print(type(sampleJson))
data = json.loads(sampleJson)
# print(type(data))
print(data["key2"])
# -------------------------------------------------------
# Exercise 3: PrettyPrint following JSON data
sampleJson = {"key1": "value1", "key2": "value2"}
json_pretty = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(json_pretty)


# -------------------------------------------------------
# Exercise 5: Access the nested key ‘salary’ from the following JSON
sampleJson = """{
   "company":{ 
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])
