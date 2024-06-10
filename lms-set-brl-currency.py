from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env-features",
        """
"PAID_COURSE_REGISTRATION_CURRENCY": ["BRL","R$"]
"""
    )
)