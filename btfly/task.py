# -*- coding: utf-8 -*-

class BaseTask(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def get_log(self):
        return self._log

    def set_log(self, log):
        self._log = log

    log = property(get_log, set_log)

    def add_arguments(self, subparsers):
        """
        Add an argument for this task.
        $ btfly csv
        """
        return subparsers.add_parser(self.name, help=self.description)

    def add_options(self, parser):
        """
        Add options for this task
        """
        pass

    def execute(self):
        pass

    def get_values(self, context):
        hosts_manager = context.hosts_manager
        values = None
        kwargs = {
            'tags': context.options.get('tags'),
            'statuses': context.options.get('statuses'),
        }
        if context.field == 'name':
            values = hosts_manager.host_names(**kwargs)
        elif context.field == 'ip':
            values = hosts_manager.ip_addresses(**kwargs)
        else:
            raise ValueError("Invalid context.field: '%s'" % (context.field))
        # TODO: check values are empty
        self.log.debug("values = %s" % (values))
        return values
