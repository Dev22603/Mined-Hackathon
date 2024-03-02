# ResumeParser : Advanced Resume Parsing Challenge (by Revelio Labs)

## Problem Statements

### Primary Challenge:
Develop a comprehensive resume parser, "ResumeRevealer," capable of extracting detailed information from resumes in various formats (PDF, JPG, HTML, DOC, etc.). The parser should accurately classify text into distinct sections (e.g., education, work experience, skills) and sequence them based on dates, where available.

### Standardization Challenge:
Enhance the "ResumeRevealer" to standardize different job titles and occupations against the O-NET database, ensuring a consistent taxonomy across parsed resumes.

### Skill Extraction
Utilizing natural language processing techniques, we extract detailed skills and competencies from resumes. In addition to parsing, the system also employs heuristic NLP techniques such as using regular expressions (regexes) to capture skills mentioned in the resumes.


## Installation and Setup

### Requirements
- Python 3.x
- TensorFlow
- Keras
- scikit-learn

### Installation
1. Clone this repository: `git clone https://github.com/your-username/ResumeRevealer.git`
2. Navigate to the project directory: `cd ResumeRevealer`
3. Install dependencies: `pip install -r requirements.txt`


## Usage
1. Ensure you have resumes to parse. Examples are provided in the repository. Adjust the file paths in `app.py` accordingly to use the provided resumes.
2. Add the path to the PDF resume you want to parse in `app.py`:
   ```python
   # GIVE ABSOLUTE PATH TO THE RESUME HERE
   ########################
   resume_path = 'your_resume.pdf'
   ########################
   ```
3. Run the parser: `python app.py`

## Features

### Text Segmentation
Automatically split the text into different parts such as education, previous work experience, skills, contact information, and job titles. The segmentation is done sequentially according to the timeline.

### Standardization of Job Titles
The project includes functionality to standardize job titles against the O-NET database. This ensures consistency and accuracy in categorizing resumes.

### Skill Extraction
Utilizing advanced natural language processing techniques, ResumeRevealer extracts detailed skills and competencies from resumes. This feature enhances candidate evaluation by highlighting specific abilities relevant to job roles.

### Matching Job Titles to O-NET Database
A machine learning script matches the obtained job titles to a standardized job list from the O-NET database, ensuring consistency and compatibility with industry standards.

## Acknowledgments
- Special thanks to Revelio Labs for their track of Advanced Resume Parsing Challenge for providing the problem statements and inspiration for this project.
- Thanks to Centre of Excellence in Data Science (Nirma University) for organizing the MINeD hackathon.
- Special thanks to Praxal Patel from Revelio Labs (the track sponsor) for his help in understanding the statement.
- Credits to the developers of TensorFlow, Keras, and scikit-learn for their invaluable tools and libraries.
