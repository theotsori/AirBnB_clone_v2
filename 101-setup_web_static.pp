# Ensure nginx is installed
package { 'nginx':
  ensure => installed,
}

# Create required directories
file { ['/data',
        '/data/web_static',
        '/data/web_static/releases',
        '/data/web_static/shared',
        '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0775',
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0644',
  content => '<html><body><h1>Hello, world!</h1></body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0775',
  require => File['/data/web_static/releases/test'],
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
",
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-available/default'],
}

