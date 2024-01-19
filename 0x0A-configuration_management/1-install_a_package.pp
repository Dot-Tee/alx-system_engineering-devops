#!/usr/bin/pup
# File: install_flask.pp
# Purpose: Install Flask version 2.1.0 using pip3
package { 'python3-pip':
  ensure => 'installed',
}
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin',
  require => Package['python3-pip'],
}
