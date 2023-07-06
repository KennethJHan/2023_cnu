patient_id = 203412
patient_id_new = "M" + str(patient_id)
print(patient_id_new, type(patient_id_new))

# patient_id = 203412
# patient_id_new = "M" + patient_id
# Traceback (most recent call last):
#   File "number_string_typecast.py", line 10, in <module>
#     patient_id_new = "M"+patient_id
# TypeError: can only concatenate str (not "int") to str

patient_id_new2 = f"M{patient_id}"
print(patient_id_new2, type(patient_id_new2))
