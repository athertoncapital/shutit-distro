"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class less(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/less')
		shutit.send('cd /tmp/build/less')
		shutit.send('wget -qO- http://www.greenwoodsoftware.com/less/less-458.tar.gz | tar -zxf -')
		shutit.send('cd less*')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/less')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return less(
		'shutit.tk.sd.less.less', 158844782.0056,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)

