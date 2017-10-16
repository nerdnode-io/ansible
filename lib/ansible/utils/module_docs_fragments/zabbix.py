# Copyright (c) 2017 Ansible, Inc
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.


class ModuleDocFragment(object):

    # Standard documentation fragment
    DOCUMENTATION = '''
options:
    validate_certs:
      required: false
      description:
       - If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
      default: true
      choices: ['true', 'false']
      version_added: "2.5"
'''
