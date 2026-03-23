import sys
try:
    import pypdf
    reader = pypdf.PdfReader("ADES - MEP profile - 190424 R4.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open("pdf_extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted text using pypdf")
except ImportError:
    print("pypdf not installed, trying PyPDF2")
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader("ADES - MEP profile - 190424 R4.pdf")
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open("pdf_extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted text using PyPDF2")
    except ImportError:
        print("Neither pypdf nor PyPDF2 installed")
        sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
