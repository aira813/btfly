conf.yaml::

  statuses:
    - active
    - troubled
    - out
    - dead
  environments:
    - { production: [ 'production', 'product', 'prd' ] }
    - { staging: [ 'staging', 'stg', 'test' ] }
    - { development: [ 'development', 'dev' ] }
  tags:
    - web: { description: 'web server' }
    - db: { description: 'database server' }
    - master_db: { description: 'master database' }
    - slave_db:  { description: 'slave database' }
    - memcached: { description: 'memcached' }
