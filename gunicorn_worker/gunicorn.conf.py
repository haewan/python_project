from main import * 
#from main import abort_worker_pid

bind = "0.0.0.0:8000"
workers = 2
loglevel = "info"
preload = True

def on_starting(server):
   	print "Starting Flask application"

def on_exit(server):
   	print "Shutting down Flask application"

def post_fork(server, worker):
        post_worker_pid(worker.pid)

def worker_abort(worker):
        abort_worker_pid(worker.pid)
