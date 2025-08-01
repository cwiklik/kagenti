# Assisted by watsonx Code Assistant
# Copyright 2025 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .. import config
from ..utils import run_command


def install():
    """Installs the Platform Operator using its Helm chart."""
    run_command(
        [
            "helm",
            "upgrade",
            "--install",
            "kagenti-platform-operator",
            "oci://ghcr.io/kagenti/kagenti-operator/kagenti-platform-operator-chart",
            "--create-namespace",
            "--namespace",
            config.OPERATOR_NAMESPACE,
            "--version",
            config.LATEST_TAG,
        ],
        "Installing the Platform Operator",
    )
