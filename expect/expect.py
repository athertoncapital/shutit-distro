"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class expect(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/expect')
		shutit.send('cd /tmp/build/expect')
		shutit.send('wget -qO- http://prdownloads.sourceforge.net/expect/expect5.45.tar.gz | tar -zxf -')
		shutit.send('cd expect*')
		shutit.send('./configure --prefix=/usr --with-tcl=/usr/lib --enable-shared --mandir=/usr/share/man --with-tclinclude=/usr/include')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('ln -svf expect5.45/libexpect5.45.so /usr/lib')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/expect')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return expect(
		'shutit.tk.sd.expect.expect', 158844782.0243,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.tcl.tcl']
	)

