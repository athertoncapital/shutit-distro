"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class onigurama(ShutItModule):


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/onigurama')
		shutit.send('cd /tmp/build/onigurama')
		shutit.send('wget -qO- http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.5.tar.gz | tar -zxf -')
		shutit.send('cd onig-5.9.5')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/onigurama')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return onigurama(
		'shutit.tk.sd.onigurama.onigurama', 158844782.0029,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)

