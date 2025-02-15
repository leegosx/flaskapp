from flask import Flask, render_template, request
import csv
import io

app = Flask(__name__)

def sort_csv(file, target_column):
    try:
        file.seek(0)
        reader = csv.DictReader(io.StringIO(file.read().decode('utf-8')))
        if target_column not in reader.fieldnames:
            raise ValueError(f"Column '{target_column}' does not exist.")
        
        # Sort the rows by the required column
        sorted_rows = sorted(reader, key=lambda row: row[target_column])

        # Write the sorted rows to a new CSV file
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)
        return output.getvalue()
    
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    if request.method == 'POST':
        uploaded_file = request.files['file']
        column = request.form['column']

        if not uploaded_file:
            return render_template('index.html', error="Please select a file.")
        
        filename = uploaded_file.filename

        sorted_csv = sort_csv(uploaded_file, column)
        
        if sorted_csv:
            return render_template('result.html', csv_data=sorted_csv, filename=filename)
        else:
            return "Error processing file", 400

    return render_template('index.html', filename=filename)

if __name__ == '__main__':
    app.run()
