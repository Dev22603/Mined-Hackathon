from parcv import parcv
import tensorflow as tf
from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model

model_path = "my_model.h5"
model = load_model(model_path)

# parser = parcv.Parser(pickle=True, load_pickled=True)
vectorizer = CountVectorizer()

# json_output = parser.parse('../../Sumedh_Nikhil_Shah_Resume.pdf')
# print(json_output)

# lines = parser.get_resume_lines()
# print(lines)

# segments = parser.get_resume_segments()
# print(segments)

# file_name = "output.json"
# parser.save_as_json(file_name)

# importing the module
import json


labeled_data = [
    (["Systems Analyst"], "Computer Systems Analyst"),
    (["Business Systems Analyst"], "Computer Systems Analyst"),
    (["Network Analyst"], "Computer Systems Analyst"),
    (["Computer Analyst"], "Computer Systems Analyst"),
    (["Software Analyst"], "Computer Systems Analyst"),
    (["IT Analyst"], "Computer Systems Analyst"),
    (["Systems Administrator"], "Computer Systems Analyst"),
    (["Computer Network Architect"], "Computer Systems Analyst"),
    (["Information Systems Analyst"], "Computer Systems Analyst"),
    (["Application Analyst"], "Computer Systems Analyst"),




    (["CEO (Chief Executive Officer)"], "Chief Executive"),
    (["President"], "Chief Executive"),
    (["Managing Director"], "Chief Executive"),
    (["Executive Director"], "Chief Executive"),
    (["Chairman"], "Chief Executive"),
    (["Director-General"], "Chief Executive"),
    (["Principal Officer"], "Chief Executive"),
    (["Chief Operating Officer (COO)"], "Chief Executive"),
    (["Chief Financial Officer (CFO)"], "Chief Executive"),
    (["Chief Information Officer (CIO)"], "Chief Executive"),




    (["Finance Manager"], "Financial Manager"),
    (["Financial Controller"], "Financial Manager"),
    (["Accounting Manager"], "Financial Manager"),
    (["Investment Manager"], "Financial Manager"),
    (["Bank Manager"], "Financial Manager"),
    (["Insurance Manager"], "Financial Manager"),
    (["Securities Manager"], "Financial Manager"),
    (["Finance Analyser"], "Financial Manager"),
    (["Branch Manager"], "Financial Manager"),
    (["Office Manager"], "Financial Manager"),



    (["Database Architect"], "Database Architect"),
    (["Data Warehouse Architect"], "Database Architect"),
    (["Database Administrator"], "Database Architect"),
    (["Data Modeler"], "Database Architect"),
    (["Database Designer"], "Database Architect"),
    (["Database Engineer"], "Database Architect"),
    (["Database Developer"], "Database Architect"),
    (["Database Analyst"], "Database Architect"),
    (["ETL Developer"], "Database Architect"),
    (["Data Warehouse Manager"], "Database Architect"),


    (["SWE"],"Software Developer"),
    (["Backend Engineer"],"Software Developer"),
    (["Frontend Developer"],"Software Developer"),
    (["Web Developer"],"Software Developer"),
    (["SDE"],"Software Developer"),
    (["Software Developement Engineer"], "Software Developer"),
    (["Software Engineer"], "Software Developer"),
    (["Software Programmer"], "Software Developer"),
    (["Application Developer"], "Software Developer"),
    (["Software Developer"], "Software Developer"),
    (["Systems Developer"], "Software Developer"),
    (["Mobile App Developer"], "Software Developer"),
    (["Embedded Software Engineer"], "Software Developer"),
    (["Full Stack Developer"], "Software Developer"),
    (["Game Developer"], "Software Developer"),



    (["Game Designer"], "Video Game Designer"),
    (["Lead Game Designer"], "Video Game Designer"),
    (["Senior Game Designer"], "Video Game Designer"),
    (["Level Designer"], "Video Game Designer"),
    (["Narrative Designer"], "Video Game Designer"),
    (["Content Designer"], "Video Game Designer"),
    (["Systems Designer"], "Video Game Designer"),
    (["Character Designer"], "Video Game Designer"),
    (["UI/UX Designer"], "Video Game Designer"),
    (["Game Writer"], "Video Game Designer"),



    (["Information Security Engineer"], "Information Security Engineer"),
    (["Cybersecurity Engineer"], "Information Security Engineer"),
    (["Network Security Engineer"], "Information Security Engineer"),
    (["Security Analyst"], "Information Security Engineer"),
    (["Security Consultant"], "Information Security Engineer"),
    (["Security Architect"], "Information Security Engineer"),
    (["Penetration Tester"], "Information Security Engineer"),
    (["Incident Responder"], "Information Security Engineer"),
    (["Forensic Analyst"], "Information Security Engineer"),
    (["Security Operations Engineer"], "Information Security Engineer"),



    (["Business Intelligence Analyst"], "Business Intelligence Analyst"),
    (["BI Analyst"], "Business Intelligence Analyst"),
    (["Market Intelligence Analyst"], "Business Intelligence Analyst"),
    (["Financial Analyst"], "Business Intelligence Analyst"),
    (["Business Analyst"], "Business Intelligence Analyst"),
    (["Reporting Analyst"], "Business Intelligence Analyst"),
    (["Analytics Consultant"], "Business Intelligence Analyst"),
    (["Data reviewer"], "Business Intelligence Analyst"),
    (["Market Research Analyst"], "Business Intelligence Analyst"),
    (["Strategic Analyst"], "Business Intelligence Analyst"),



    (["Electrical Engineer"], "Electrical Engineer"),
    (["Senior Electrical Engineer"], "Electrical Engineer"),
    (["Power Systems Engineer"], "Electrical Engineer"),
    (["Control Systems Engineer"], "Electrical Engineer"),
    (["Hardware Engineer"], "Electrical Engineer"),
    (["RF Engineer"], "Electrical Engineer"),
    (["Instrumentation Engineer"], "Electrical Engineer"),
    (["Automation Engineer"], "Electrical Engineer"),
    (["Embedded Systems Engineer"], "Electrical Engineer"),
    (["Test Engineer"], "Electrical Engineer"),



    (["Manufacturing Engineer"], "Manufacturing Engineer"),
    (["Senior Manufacturing Engineer"], "Manufacturing Engineer"),
    (["Process Engineer"], "Manufacturing Engineer"),
    (["Industrial Engineer"], "Manufacturing Engineer"),
    (["Production Engineer"], "Manufacturing Engineer"),
    (["Quality Engineer"], "Manufacturing Engineer"),
    (["Continuous Improvement Engineer"], "Manufacturing Engineer"),
    (["Operations Engineer"], "Manufacturing Engineer"),
    (["Lean Manufacturing Engineer"], "Manufacturing Engineer"),
    (["Product Engineer"], "Manufacturing Engineer"),



    (["ML enthusiast"],"Data Scientist"),
    (["ML Engineer"],"Data Scientist"),
    (["Data Scientist"], "Data Scientist"),
    (["Senior Data Scientist"], "Data Scientist"),
    (["Machine Learning Engineer"], "Data Scientist"),
    (["Data Analyst"], "Data Scientist"),
    (["Quantitative Analyst"], "Data Scientist"),
    (["Research Scientist"], "Data Scientist"),
    (["Big Data Engineer"], "Data Scientist"),
    (["AI Engineer"], "Data Scientist"),
    (["Statistical Analyst"], "Data Scientist"),
    (["Deep Learning Engineer"], "Data Scientist")


]



job_category_to_ONET_SOC = {}
job_category_to_ONET_SOC["Computer Systems Analyst"] = "15-1211.00"
job_category_to_ONET_SOC["Chief Executive"] = "11-1011.00"
job_category_to_ONET_SOC["Data Scientist"] = "15-2051.00"
job_category_to_ONET_SOC["Manufacturing Engineer"] = "17-2112.03"
job_category_to_ONET_SOC["Electrical Engineer"] = "17-2071.00"
job_category_to_ONET_SOC["Business Intelligence Analyst"] = "15-2051.01"
job_category_to_ONET_SOC["Information Security Engineer"] = "15-1212.00"
job_category_to_ONET_SOC["Video Game Designer"] = "15-1255.01"
job_category_to_ONET_SOC["Software Developer"] = "15-1252.00"
job_category_to_ONET_SOC["Database Architect"] = "15-1243.00"
job_category_to_ONET_SOC["Financial Manager"] = "11-3031.00"

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model



from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

job_titles = []
# Extract features and labels from the labeled data
for title in labeled_data:
  for word in title[0]:
    job_titles.append(word)
labels = [label[1] for label in labeled_data]
# Convert labels into numerical representation
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
num_classes = len(label_encoder.classes_)

# Convert job titles into count vectors
ct_vectorizer = CountVectorizer()
ct_vectorizer.fit(job_titles)
X = ct_vectorizer.transform(job_titles)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, encoded_labels, test_size=0.2, random_state=42)

# Build a simple neural network
model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=150, batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy:", accuracy)

 
# Opening JSON file
with open('output.json') as json_file:
    data = json.load(json_file)

    standardized_output = [];

    for jobs in data["Job History"]:
        new_job_titles = [jobs["Job Title"]]
        print(new_job_titles)
        new_job_titles_vectorized = ct_vectorizer.transform(new_job_titles)
        predictions = model.predict(new_job_titles_vectorized)
        print(predictions)
        predicted_labels = label_encoder.inverse_transform(np.argmax(predictions, axis=1))
        print("Requirements:", new_job_titles)
        print("Predictions:", predicted_labels)
        print("Corresponding O*NET-SOC 2019 codes are : ")
        for label in predicted_labels:
            standardized_output.append(job_category_to_ONET_SOC[label])

    print(standardized_output)