from fabric.api import env, run

env.hosts = ['localhost']

def test():
	run("python ~/reading-list/app.py")
