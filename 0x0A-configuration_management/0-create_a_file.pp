# Create a Puppet manifest file, e.g., create_file.pp

file { '/tmp/school':
  ensure   => 'file',
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
  content  => 'I love Puppet',
}
