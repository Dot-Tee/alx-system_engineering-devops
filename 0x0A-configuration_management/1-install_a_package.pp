#!usr/bin/pup
# Create a Puppet manifest file

package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => package['python3-pip'],
}