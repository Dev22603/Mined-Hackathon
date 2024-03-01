from parcv import parcv

parser = parcv.Parser(pickle=True, load_pickled=True)

json_output = parser.parse('../Sumedh_Nikhil_Shah_Resume.pdf')
print(json_output)

lines = parser.get_resume_lines()
print(lines)

segments = parser.get_resume_segments()
print(segments)

file_name = "output.json"
parser.save_as_json(file_name)