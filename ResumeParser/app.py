from parcv import parcv
import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pdfplumber
import re
import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from keras.utils import to_categorical

parser = parcv.Parser(pickle=True, load_pickled=True)
vectorizer = CountVectorizer()


# GIVE ABSOLUTE PATH TO THE RESUME HERE
########################
resume_path = '/Users/vatsal/Desktop/untitled folder/Mined-Hackathon/Resume Validation Set/easy_level1b.pdf'
########################

json_output = parser.parse(resume_path)
print(json_output)

lines = parser.get_resume_lines()
print(lines)

segments = parser.get_resume_segments()
print(segments)

file_name = "output.json"

parser.save_as_json(file_name)

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



    (["sde"],"Software Developer"),
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


 
 
# Opening JSON file
with open('output.json', "r+") as json_file:
    data = json.load(json_file)

    standardized_output = []

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
            standardized_output.append(label)

    print(standardized_output)
    data["Standardized Job Titles"] = standardized_output
    # Reset file pointer to beginning before writing
    

    # To catch skills not caught by the parser
    if len(data['Skills'])==0:
        
        text_data = ''
        with pdfplumber.open(resume_path) as pdf:
            for page in pdf.pages:
                text_data += page.extract_text()
        skills_list = [
        "Java",
        "Python",
        "C/C++",
        "JavaScript",
        "Ruby",
        "Swift",
        "Kotlin",
        "Go",
        "PHP",
        "SQL",
        "HTML/CSS",
        "React",
        "Angular",
        "Vue.js",
        "Node.js",
        "RESTful APIs",
        "Git",
        "Docker",
        "Linux",
        "AWS",
        "Azure",
        "Google Cloud Platform",
        "CI/CD",
        "Agile Methodologies",
        "Scrum",
        "Kubernetes",
        "Microservices",
        "Data Structures",
        "Algorithms",
        "Object-Oriented Programming",
        "Functional Programming",
        "Test-Driven Development (TDD)",
        "Continuous Integration (CI)",
        "Continuous Deployment (CD)",
        "DevOps",
        "Backend Development",
        "Frontend Development",
        "Full-Stack Development",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing (NLP)",
        "Computer Vision",
        "Big Data",
        "Data Mining",
        "Data Analysis",
        "Data Visualization",
        "Database Management",
        "NoSQL Databases",
        "Relational Databases",
        "MongoDB",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "Redis",
        "Elasticsearch",
        "Apache Kafka",
        "Hadoop",
        "Spark",
        "Scala",
        "TensorFlow",
        "PyTorch",
        "Keras",
        "OpenCV",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Jupyter Notebook",
        "GitLab",
        "Jira",
        "Confluence",
        "Trello",
        "Visual Studio Code",
        "PyCharm",
        "IntelliJ IDEA",
        "Sublime Text",
        "Eclipse",
        "NetBeans",
        "Visual Studio",
        "Atom",
        "Bash Scripting",
        "PowerShell",
        "Shell Scripting",
        "REST API",
        "GraphQL",
        "OAuth",
        "JWT",
        "TCP/IP",
        "HTTP/HTTPS",
        "DNS",
        "SSH",
        "SSL/TLS",
        "OAuth",
        "JWT",
        "Blockchain",
        "Smart Contracts",
        "Solidity",
        "Ethereum",
        "Web3.js",
        "Cryptocurrency",
        "Cybersecurity",
        "Penetration Testing",
        "Ethical Hacking",
        "Firewalls",
        "Intrusion Detection Systems",
        "Security Auditing",
        "Security Policies",
        "Vulnerability Assessment",
        "Security Incident Response",
        "Security Information and Event Management (SIEM)",
        "Threat Intelligence",
        "Identity and Access Management (IAM)",
        "Encryption",
        "Network Security",
        "Application Security",
        "Cloud Security",
        "Endpoint Security",
        "Security Compliance",
        "Security Architecture",
        "Secure Coding Practices",
        "Disaster Recovery Planning",
        "Business Continuity Planning",
        "Risk Management",
        "Compliance Management",
        "IT Governance",
        "ITIL",
        "ISO/IEC 27001",
        "NIST Cybersecurity Framework",
        "PCI DSS",
        "GDPR",
        "HIPAA",
        "SOX Compliance",
        "Agile Methodologies",
        "Scrum",
        "Kanban",
        "Lean Software Development",
        "Pair Programming",
        "Agile Testing",
        "Agile Project Management",
        "Agile Estimation and Planning",
        "Agile Retrospectives",
        "Agile User Stories",
        "Agile Sprints",
        "Agile Continuous Integration (CI)",
        "Agile Continuous Deployment (CD)",
        "Agile DevOps",
        "Agile Product Backlog Management",
        "Agile Sprint Reviews",
        "Agile Sprint Planning",
        "Agile Daily Stand-ups",
        "Agile Scrum Master",
        "Agile Product Owner",
        "Agile Team Facilitation",
        "Agile Coaching",
        "Agile Leadership",
        "Agile Transformation",
        "Agile Metrics and KPIs",
        "Agile Risk Management",
        "Agile Stakeholder Engagement",
        "Agile Change Management",
        "Agile Release Management",
        "Agile Tools and Techniques",
        "Agile Principles and Values",
        "Agile Manifesto",
        "Agile Practices",
        "Agile Culture",
        "Microsoft Word",
        "Powerpoint",
        "Power Bi"
    ]

        skills_found = []
        for skill in skills_list:
            # Escape special characters in the skill name
            escaped_skill = re.escape(skill)
            # Use regular expressions to find the skill in the resume text.
            if re.search(escaped_skill, text_data, flags=re.IGNORECASE):
                skills_found.append(skill)

        
        data['Skills'] = skills_found

    json_file.seek(0)
    json.dump(data, json_file, indent=4, default=str, ensure_ascii=False)
    # Truncate remaining content to ensure data consistency
    json_file.truncate()



