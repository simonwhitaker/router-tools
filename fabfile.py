from fabric.api import env, run

PPPOE0='pppoe0'

env.hosts = ['192.168.1.1']
env.shell = '/bin/vbash --login -c'

def _run_edgeos(command):
    run('/opt/vyatta/bin/vyatta-op-cmd-wrapper %s' % command)

def disconnect(interface=PPPOE0):
    _run_edgeos('disconnect interface %s' % interface)

def connect(interface=PPPOE0):
    _run_edgeos('connect interface %s' % interface)

def reconnect(interface=PPPOE0):
    disconnect()
    connect()
