# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default filed
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

# Restart Nginx
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
