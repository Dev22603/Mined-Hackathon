import os
import pypandoc

class ResumeConverter:
    def __init__(self, docx_filename):
        self.docx_filename = docx_filename

    def convert_to_plain_text(self):
        try:
            # Extracting the base name (without extension) of the DOCX file
            base_name = os.path.splitext(self.docx_filename)[0]
            txt_filename = f"{base_name}.txt"
            
            output = pypandoc.convert_file(self.docx_filename, 'plain', outputfile=txt_filename)
            return f"Conversion successful. Plain text saved to: {txt_filename}"
        except Exception as e:
            return f"Error: {e}"

docx_filename = 'Resume.docx'

resume_converter = ResumeConverter(docx_filename)
result = resume_converter.convert_to_plain_text()
print(result)
