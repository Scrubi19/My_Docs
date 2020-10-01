Ruby on Rails
====================

Установка на Ubuntu
~~~~~~~~~~~~~~~~~~~~~~

1. Установить rbenv

.. code-block:: bash

  git clone https://github.com/rbenv/rbenv.git ~/.rbenv


2. Вписать зависимости

.. code-block:: bash

  echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(rbenv init -)"' >> ~/.bashrc
  exec $SHELL

3. Установить ruby-build
 
.. code-block:: bash
 
  git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build

4. Установить ruby

.. code-block:: bash

  rbenv install 2.7.1
  rbenv global 2.7.1

Пример Gemfile:

.. code-block:: bash

  source 'https://rubygems.org'

  ruby '2.7.1'

  gem 'colorize'
  gem 'csv'
  gem 'rails'
  gem 'rspec'
  gem 'rubocop'
  gem 'simplecov'

Команды:


.. code-block:: bash

  bundle install - установка gem-ов из Gemfile
  bundle exec rubocop - запуск rubocop
  bundle exec rspec - запуск тестов
  
