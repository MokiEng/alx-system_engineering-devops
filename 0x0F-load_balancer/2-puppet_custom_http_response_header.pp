# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
        listen 80 default_server;
        server_name _;
        location / {
            add_header X-Served-By $hostname;
            # Your site configuration goes here
        }
    }
  ',
  require => Package['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx after making changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
