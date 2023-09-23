# configure ssh config


file_line {'use private key in path':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentification no'
}

file_line {'identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school'
}
