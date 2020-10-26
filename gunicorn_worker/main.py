import os
from flask import Flask
import redis
from redis.sentinel import Sentinel

app = Flask(__name__)

sentinel = Sentinel([('192.168.100.135', 26379),
                     ('192.168.100.245', 26379),
                     ('192.168.100.143', 26379)
                    ],
                    socket_timeout=0.5)

@app.route("/")
def hello():
    return "Hello from Flask Python"

@app.route("/set")
def set_redis():  
    master = get_master()
    w_ret = master.set('foo', 'bar')
    return "master set"

@app.route("/get")
def get_redis():
    slave = get_slave()
    r_ret = slave.get('foo')
    return r_ret 

def get_master():
    master = sentinel.master_for('mymaster', socket_timeout=0.5, db=15)
    return master

def get_slave(): 
    slave = sentinel.slave_for('mymaster', socket_timeout=0.5, db=15)
    return slave

def post_worker_pid(worker_pid):
    print ("#######post_worker_pid######")
    print (worker_pid)
    print ("#######post_worker_pid######")

def abort_worker_pid(worker_pid):
    print ("#######abort_worker_pid######")
    print (worker_pid)
    print ("#######abort_worker_pid######")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
