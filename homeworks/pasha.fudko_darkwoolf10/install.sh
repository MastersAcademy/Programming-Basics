#!/usr/bin/env bash

echo '---===   UPDATING BEGIN   ===---'
sudo apt-get update && sudo apt-get upgrade
echo '---===   UPDATING  END    ===---'

echo '---=== PYENV REQUIREMENTS INSTALLATION BEGIN ===---'
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
echo '---=== PYENV REQUIREMENTS INSTALLATION  END  ===---'

echo '---=== PYENV INSTALLATION BEGIN  ===---'
su -l ubuntu -c 'curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash'
echo '---=== PYENV INSTALLATION  END   ===---'

# vim .bash_profile
#
# export PATH="~/.pyenv/bin:$PATH"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"

# echo 'cd /vagrant' >> ~/.bash_profile
