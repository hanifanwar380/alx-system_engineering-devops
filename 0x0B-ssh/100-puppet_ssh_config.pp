# SSH Client configurations so that we can connect to a server without using a password

include stdlib
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Turn off pubkey auth':
  path    => '/etc/ssh/ssh_config',
  line    => '    PubkeyAuthentication yes',
  replace => true,
}
