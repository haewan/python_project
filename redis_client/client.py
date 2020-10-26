import redis
from redis.sentinel import Sentinel

if __name__ == '__main__':

    try:
        sentinel = Sentinel([('192.168.100.135', 26379),
                             ('192.168.100.245', 26379),
                             ('192.168.100.143', 26379)
                             ],
                            socket_timeout=0.5)

        master = sentinel.discover_master('mymaster')
        print(master)

        slave = sentinel.discover_slaves('mymaster')
        print(slave)

        master = sentinel.master_for('mymaster', socket_timeout=0.5, db=15)
        w_ret = master.set('foo', 'bar')

       # slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='redis_auth_pass', db=15)
        slave = sentinel.slave_for('mymaster', socket_timeout=0.5, db=15)
        r_ret = slave.get('foo')
        print(r_ret)

    except Exception as e:
        print(e)
