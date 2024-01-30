# Apply the configuration
exec { 'update ulimit':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => 'shell',
}

exec { 'nginx restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
