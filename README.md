## ansible-plugins

A collection of (possibly) usefull Ansible plugins.

### HowTo

Normally, in order to make Ansible scan your custom plugin directories, you should
provide the proper paths inside the `defaults` section of your active `ansible.cfg` file.
See also the docs on [The Ansible Configuration File](http://docs.ansible.com/intro_configuration.html).

For example, if you checkout this repository to an `ansible_plugins` folder of your main project
(e.g. as a git submodule), you could provide a similar configuration:

```ini
[defaults]

# other settings ...

filter_plugins = ./ansible_plugins/filter_plugins:/usr/local/share/ansible_plugins/filter_plugins
lookup_plugins = ./ansible_plugins/lookup_plugins:/usr/local/share/ansible_plugins/lookup_plugins
```
