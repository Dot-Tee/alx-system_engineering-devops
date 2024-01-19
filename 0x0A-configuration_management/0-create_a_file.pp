# Creating a Puppet manifest file, e.g create_file.pp
file { '/tmp/school':
	ensure	=> 'file',
	path	=> '/tmp/school',
	mode	=> '0744',
	owner	=> 'www-data',
	group	=> 'www-data',
	content	=> 'I love Puppet',
}
