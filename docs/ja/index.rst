.. btfly documentation master file, created by
   sphinx-quickstart on Sat Dec  3 19:05:02 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

btfly |release| documentation
=============================

What is btfly?
--------------
btflyはYAMLまたはJSON形式のファイルにサーバの情報を記述して、大量のサーバ群の管理を容易にするためのコマンド兼フレームワークである。

簡単な例
--------

.. include:: ../_conf_yaml.all.rst
.. include:: ../_hosts_yaml.all.rst

.. highlight:: bash

まず上記の conf.yaml と hosts.yaml を conf ディレクトリに作成しておく。そして btfly コマンドを実行する ::

  $ btfly out

これにより::

  web01 db01 db02 db03

が出力される。この出力を利用することで、全てのサーバに ssh で uptime を実行することが可能になる。 ::

  $ for host in `btfly out`; do ssh $host uptime; done

つまり、自分が管理するホスト情報を hosts.yaml に書いておくことで、そのホスト群に対してコマンドを発行するなどの連携が可能になる。また、独自プラグインを書くことで、ホスト群の情報をもとに /etc/hosts のファイルを生成することも可能である。


条件をつけてホストを絞り込む
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

--tags ::

  $ btfly --tags=db out
  >>> db01 db02 db03

とすることで --tags で指定したタグのホストのみを抽出することもできる。カンマ区切りで複数のタグを指定することも可能である。

--statuses ::

  $ btfly --statuses=active out
  >>> web01 db01 db02

とすれば status が active なホストだけを抽出できる。これにより「故障中のサーバは除外したい」ということも可能である。

プラグインによる機能追加
^^^^^^^^^^^^^^^^^^^^^^^^

Pythonでプラグインを書くことで ::

  $ btfly --your-plugin-option your_plugin

のように呼び出すことができるので、例えば `Munin <http://munin-monitoring.org/>`_ の設定ファイルを生成するプラグインを作成することも可能である。

まとめ
^^^^^^

btflyを使ってサーバのステータスや役割の管理を行うようにすれば

* 特定のホストにだけコマンドを流す
* 特定のホストにファイルをリリースする

が可能になる。

Contents:
---------
.. toctree::
   :maxdepth: 2

   install
   tutorial
   btfly
   plugin

Indices and tables
==================
.. * :ref:`genindex`
.. * :ref:`modindex`
* :ref:`search`
