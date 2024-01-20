# Replacing 'phpp' with 'php' extantion in 'wp-settings.php'

exec { 'fixing-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
