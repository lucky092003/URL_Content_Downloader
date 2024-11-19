from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def download_url_content(url, output_file):
    """
    Downloads content from a given URL and saves it to a specified file.
    """
    try:
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        with open(output_file, 'wb') as file:
            file.write(response.content)  # Save the content to the file

        return f"Content successfully downloaded and saved to: {output_file}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred while downloading content: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL and output file path from the form
        url = request.form['url']
        output_file = request.form['output_file']
        
        # Call the function to download content
        result = download_url_content(url, output_file)
        
        return render_template('index.html', result=result)
    
    return render_template('index.html', result=None)

if __name__ == "__main__":
    app.run(debug=True)
