from flask import Flask, render_template
from flask_socketio import SocketIO
import psutil
import json
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def get_system_info():
  cpu_usage = psutil.cpu_percent(interval=1)
  memory = psutil.virtual_memory()
  disk = psutil.disk_usage('/')
  net = psutil.net_io_counters()

  system_info = {
    "cpu_usage_percent": cpu_usage,
    "memory_total": memory.total,
    "memory_available": memory.available,
    "memory_percent": memory.percent,
    "disk_total": disk.total,
    "disk_used": disk.used,
    "disk_percent": disk.percent,
    "network_sent": net.bytes_sent,
    "network_recv": net.bytes_recv,
  }
  return system_info

def emit_system_info():
  while True:
    system_info = get_system_info()
    socketio.emit('system_info', json.dumps(system_info), namespace='/')
    time.sleep(5)

if __name__ == '__main__':
  socketio.start_background_task(emit_system_info)
  socketio.run(app, debug=True)