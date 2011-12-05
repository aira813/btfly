.. btfly documentation master file, created by
   sphinx-quickstart on Sat Dec  3 19:05:02 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

btfly |release| documentation
=============================

What is btfly?
--------------
btflyはYAMLまたはJSON形式のファイルにサーバの情報を記述して、大量のサーバ群を管理することを容易にするためのフレームワーク。

簡単な例
--------

hosts.yaml::

  roles:
    - web: { description: 'web server' }
    - master_db: { description: 'master database' }
    - slave_db:  { description: 'slave database' }
    - memcached: { description: 'memcached' }
  hosts:
    - web01: { ip: '192.168.1.10', status: 'active', roles: [ 'web', 'memcached' ] }
    - db01:  { ip: '192.168.1.50', status: 'active', roles: [ 'master_db' ] }
    - db02:  { ip: '192.168.1.60', status: 'active', roles: [ 'slave_db' ] }
    - db03:  { ip: '192.168.1.61', status: 'out',    roles: [ 'slave_db' ] }

.. highlight:: bash

まず上記の hosts.yaml を conf ディレクトリに作成しておく。そして btfly コマンドを実行する ::

  $ btfly env

これにより::

  BTFLY_HOSTS=(web01 db01 db02 db03)

が出力される。この出力をevalすることで、全てのサーバに ssh で uptime を実行することが可能になる。 ::

  $ eval `btfly env`
  $ for host in ${BTFLY_HOSTS[@]}; do ssh $host uptime; done

条件をつける
^^^^^^^^^^^^

--roles ::

  $ eval `btfly env --roles slave_db`
  $ echo $BTFLY_HOSTS
  >>> db02 db03

とすることで --roles で指定したロールを持つホストのみを抽出することもできる。

--statuses ::

  $ eval `btfly env --statuses active
  $ echo $BTFLY_HOSTS
  >>> web01 db01 db02

とすれば status が active なホストだけを抽出できる。これにより「故障中のサーバは除外したい」ということも可能である。

まとめ
^^^^^^

btflyを使ってサーバのステータスや役割の管理を行うようにすれば

* 特定のホストにだけコマンドを流す
* 特定のホストにファイルをリリースする

が可能になる。また、Pythonでプラグインを書くことで ::

  $ btfly your_plugin --your-option

のように呼び出すことができるので、例えば `Nagios <http://www.nagios.org>`_ の設定ファイルを生成するプラグインを作成することも可能である。


Contents:
---------

.. toctree::
   :maxdepth: 2

   quick_start


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
