from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

def read_json_file(file_path):
    """Reads a JSON file and returns its contents."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    """Render the home page."""
    return "<h1>Welcome to the JSON Reader App</h1><p>Go to <a href='/data'>/data</a> to view the JSON data.</p>"

@app.route('/data')
def data():
    """Display the contents of the JSON file."""
    file_path = 'data.json'  # Specify the path to your JSON file
    json_data = read_json_file(file_path)
    return render_template('data.html', data=json_data)

if __name__ == "__main__":
    app.run(debug=True)
