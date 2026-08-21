# Copyright 2025 IBM Corp.
# Licensed under the Apache License, Version 2.0

"""
Helpers for deriving valid Kubernetes resource names from user-supplied text.
"""

# RFC-1123 DNS label — the shape of a Kubernetes resource / namespace name:
# lowercase alphanumeric plus '-', starting and ending with an alphanumeric.
# Use with FastAPI ``Path(pattern=K8S_NAME_PATTERN, max_length=K8S_NAME_MAX_LENGTH)``
# to constrain user-supplied path params at the boundary, so injection characters
# (e.g. an encoded newline) can't reach loggers or downstream calls — invalid input
# is rejected with 422 before any handler code runs. (rossoctl/rossoctl#2395)
K8S_NAME_PATTERN = r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"
K8S_NAME_MAX_LENGTH = 63


def sanitize_k8s_name(name: str) -> str:
    """Sanitize a name to be valid for Kubernetes resource names.

    Falls back to ``"resource"`` when the input sanitizes to nothing (empty or
    all-punctuation), since a Kubernetes name may not be empty.
    """
    out = "".join(c.lower() if c.isalnum() or c in ("-", ".") else "-" for c in name)
    out = out.strip("-.")
    return out or "resource"
