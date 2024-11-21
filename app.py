from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def download_url_content(url, output_file):
    """
    Downloads content from a given URL and saves it to a specified file.
    """
    try:
        response = requests.get(url)  
        response.raise_for_status()  

        with open(output_file, 'wb') as file:
            file.write(response.content)  

        return f"Content successfully downloaded and saved to: {output_file}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred while downloading content: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        url = request.form['url']
        output_file = request.form['output_file']
        
        result = download_url_content(url, output_file)
        
        return render_template('index.html', result=result)
    
    return render_template('index.html', result=None)

if __name__ == "__main__":
    app.run(debug=True)
