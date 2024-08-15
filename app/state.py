class StateManager:
    def __init__(self):
        self.pdfs = {}

    def add_pdf(self, pdf_id, pdf_content):
        self.pdfs[pdf_id] = pdf_content

    def get_pdf(self, pdf_id):
        return self.pdfs.get(pdf_id)
