from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items([
    (
        "common-env-features",
        '"ENABLE_THIRD_PARTY_AUTH": true',
    ),
    (
        "openedx-lms-common-settings",
        """
# saml special settings
AUTHENTICATION_BACKENDS += ["common.djangoapps.third_party_auth.saml.SAMLAuthBackend", "django.contrib.auth.backends.ModelBackend"]
"""
    ),
    (
        "openedx-auth",
        """
"SOCIAL_AUTH_SAML_SP_PRIVATE_KEY": "yoursecretkey",
"SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "yourpubliccert"
        """
    ),
])