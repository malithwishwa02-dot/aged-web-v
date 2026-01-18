from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import threading
import uuid
import time
import os
import json
from core.ai_orchestrator import AI_Orchestrator

app = Flask(__name__, template_folder='templates')
CORS(app)

JOBS = {}
LOGS = {}
OUTPUT_DIR = os.path.join(os.getcwd(), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

<<<<<<< HEAD
@app.route('/api/spawn', methods=['POST'])
def spawn_agent():
    data = request.get_json()
    target = data.get('target')
    persona = data.get('persona')
    job_id = str(uuid.uuid4())
    LOGS[job_id] = []
    def log_callback(msg):
        LOGS[job_id].append({'timestamp': time.time(), 'msg': msg})
    def run_job():
        JOBS[job_id] = 'RUNNING'
        orchestrator = AI_Orchestrator(job_id, target, log_callback)
        result = orchestrator.run_aging_cycle()
        JOBS[job_id] = 'SUCCESS' if result == 'SUCCESS' else 'FAILED'
    thread = threading.Thread(target=run_job, daemon=True)
    thread.start()
    return jsonify({'job_id': job_id, 'status': 'SPAWNED'})

@app.route('/api/status/<job_id>', methods=['GET'])
def status(job_id):
    return jsonify({'logs': LOGS.get(job_id, []), 'status': JOBS.get(job_id, 'UNKNOWN')})

@app.route('/api/download/<job_id>', methods=['GET'])
def download(job_id):
    filename = f'{job_id}_soul.zip'
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False, port=5000, threaded=True)
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import threading
import uuid
import time
import os
import json
from core.ai_orchestrator import AI_Orchestrator

app = Flask(__name__, template_folder='templates')
CORS(app)

JOBS = {}
LOGS = {}
OUTPUT_DIR = os.path.join(os.getcwd(), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

=======
>>>>>>> c8dd0d8 (CHRONOS V2026: Core Initialization - Level 9 Modules Active)
@app.route('/api/spawn_agent', methods=['POST'])
def spawn_agent():
    data = request.get_json()
    target = data.get('target')
    persona = data.get('persona')
<<<<<<< HEAD
=======
    identity = data.get('identity')
    mode = data.get('mode', None)
>>>>>>> c8dd0d8 (CHRONOS V2026: Core Initialization - Level 9 Modules Active)
    job_id = str(uuid.uuid4())
    LOGS[job_id] = []
    def log_callback(msg):
        LOGS[job_id].append({'timestamp': time.time(), 'msg': msg})
    def run_job():
        JOBS[job_id] = 'RUNNING'
<<<<<<< HEAD
        orchestrator = AI_Orchestrator(job_id, target, log_callback)
=======
        orchestrator = AI_Orchestrator(job_id, target, log_callback, identity=identity, mode=mode)
>>>>>>> c8dd0d8 (CHRONOS V2026: Core Initialization - Level 9 Modules Active)
        result = orchestrator.run_aging_cycle()
        JOBS[job_id] = 'COMPLETED' if result == 'SUCCESS' else 'FAILED'
    thread = threading.Thread(target=run_job, daemon=True)
    thread.start()
    return jsonify({'job_id': job_id, 'status': 'SPAWNED'})

@app.route('/api/status/<job_id>', methods=['GET'])
def status(job_id):
    return jsonify({'logs': LOGS.get(job_id, []), 'status': JOBS.get(job_id, 'UNKNOWN')})

@app.route('/api/download/<job_id>', methods=['GET'])
def download(job_id):
    filename = f'{job_id}_profile.zip'
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
