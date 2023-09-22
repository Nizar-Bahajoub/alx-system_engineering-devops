#kill a process

exec { 'pkill':
  command  => '/usr/bin/pkill -SIGTERM killmenow',
}
