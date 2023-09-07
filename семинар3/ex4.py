# Напишите программу для печати всех уникальных значений в словаре.

list_1 = [{"V": "S001"}, {"V": "S002"}, 
          {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

result = []
for element in list_1:
    for k,v in element.items():
        result.append(v)
print(result)
print(set(result))
