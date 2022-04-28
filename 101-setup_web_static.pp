# Refacto of Task 0 but using puppet

exec {'sudo-apt-get-update':
  ensure  => 'absent',
  require => Exec['apt-get-update']
}

package { 'nginx':
  ensure  => 'installed',
  require => Package['apache2.2-common']
}

service {'nginx':
  ensure  => 'running',
  require => file_line['ADDING LOCATION']
}

file { ['/data', '/data/web_static', '/data/web_static/shared', '/data/web_static/releases', '/data/web_static/releases/test']:
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => Package['nginx']
}


file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'This is my sample content',
  require =>  Package['nginx']
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true
}

file_line { 'ADDING A LOCATION':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => 'location /hbnb_static/ { alias /data/web_static/current/; autoindex off; } location / { ',
  match   => '^\s+location+',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
