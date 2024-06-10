from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "common-env-features",
        """
"CUSTOM_CERTIFICATE_TEMPLATES_ENABLED": true,
"ORGANIZATIONS_APP": true,
"""
    )
)