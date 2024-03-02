# ResumeRevealer: Advanced Resume Parsing Challenge

## Problem Statements

### Primary Challenge:
Develop a comprehensive resume parser, "ResumeRevealer," capable of extracting detailed information from resumes in various formats (PDF, JPG, HTML, DOC, etc.). The parser should accurately classify text into distinct sections (e.g., education, work experience, skills) and sequence them based on dates, where available.

### Standardization Challenge:
Enhance the "ResumeRevealer" to standardize different job titles and occupations against the O-NET database, ensuring a consistent taxonomy across parsed resumes.

### Skill Extraction Challenge:
Implement an advanced feature in "ResumeRevealer" that mines detailed skills and competencies from project descriptions and position roles within the resume, highlighting the candidate's specific abilities and expertise. Abstractive skill extraction is a bonus.

## Installation and Setup

### Requirements
- Python 3.x
- TensorFlow
- Keras
- scikit-learn
- parcv library (if not installed, use `pip install parcv`)

### Installation
1. Clone this repository: `git clone https://github.com/your-username/ResumeRevealer.git`
2. Navigate to the project directory: `cd ResumeRevealer`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

### Training the Model
1. Ensure you have labeled data for training. Adjust the `labeled_data` variable in `train_model.py` with your data.
2. Run the training script: `python train_model.py`

### Running the Parser
1. Ensure you have resumes to parse. Adjust the file paths in `main.py` accordingly.
2. Run the parser: `python main.py`

## Advanced Features

### Standardization of Job Titles
The project includes functionality to standardize job titles against the O-NET database. This ensures consistency and accuracy in categorizing resumes.

### Skill Extraction
Utilizing advanced natural language processing techniques, ResumeRevealer extracts detailed skills and competencies from resumes. This feature enhances candidate evaluation by highlighting specific abilities relevant to job roles.

## Contributing
We welcome contributions to ResumeRevealer! If you have ideas for improvement or want to report bugs, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to the organizers of the Advanced Resume Parsing Challenge for providing the problem statements and inspiration for this project.
- Credits to the developers of TensorFlow, Keras, and scikit-learn for their invaluable tools and libraries.
