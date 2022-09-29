# Configure and prepare web servers

package { 'nginx':
  ensure   => 'present',
  provider = 'apt'
}

file { ['/data/web_static/shared/', '/data/web_static/releases/test/']:
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Hello ALX'
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/'
}
file { '/data/':
group => 'ubuntu',
owner => 'ubuntu'
}
exec {
  command => 'sudo sed -i '44 a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default',
  path => '/usr/bin/:usr/local/bin/:/bin/'
}
exec { 'nginx restart':
  path => 'etc/init.d/'
}
