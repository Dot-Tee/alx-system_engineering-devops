# Create a Puppet manifest file, e.g., kill_process.pp

exec { 'killmenow_process':
  command     => 'pkill -f "killmenow"',
  path        => '/usr/local/bin:/usr/bin',
  logoutput   => true,
  refreshonly => true,
}
