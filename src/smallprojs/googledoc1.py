import requests

# URL of the Google Doc
google_doc_url = "https://docs.google.com/document/u/0/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub?pli=1"

# Specify the format you want to download the document in (e.g., PDF, DOCX)
download_url = google_doc_url.replace('/pub', '/export') + '?format=pdf'  # Change 'pdf' to 'docx' for DOCX format

download_url = "https://docs.google.com/document/u/0/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/export?format=pdf"
published_url = "https://docs.google.com/document/u/0/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub?pli=1"


# Send a GET request to download the document
response = requests.get(published_url)

# Check if the request was successful
if response.status_code == 200:
    # Save the document to a local file
    with open('downloaded_doc.html', 'wb') as file:  # Change the filename and extension as needed
        file.write(response.content)
    print("Document downloaded successfully!")
else:
    print("Failed to download the document. Status code:", response.status_code)
