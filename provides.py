# Copyright 2017 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

from charmhelpers.core.hookenv import config

from charms.reactive import (
    Endpoint,
    when)


class KeystoneFederatedBackendProvides(Endpoint):

    scope = scopes.GLOBAL

    @when('{provides:keystone-federated-backend}-relation-joined')
    def set_relation_info(self):
        self.set_remote(**config())

    def trigger_restart(self):
        """
        Trigger a restart of keystone
        """
        relation_info = {
            'restart-nonce': str(uuid.uuid4())
        }
        self.set_remote(**relation_info)
