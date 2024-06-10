from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items([
    (
        "lms-env",
        """
"COURSE_MODE_DEFAULTS": {
    "name": "Honor",
    "slug": "honor",
    "bulk_sku": null,
    "android_sku": null,
    "ios_sku": null,
    "currency": "BRL",
    "description": null,
    "expiration_datetime": null,
    "min_price": 0,
    "sku": null,
    "suggested_prices": ""
  }
"""
    ),
    
     (
        "cms-env",
        """
"COURSE_MODE_DEFAULTS": {
    "name": "Honor",
    "slug": "honor",
    "bulk_sku": null,
    "android_sku": null,
    "ios_sku": null,
    "currency": "BRL",
    "description": null,
    "expiration_datetime": null,
    "min_price": 0,
    "sku": null,
    "suggested_prices": ""
  }
"""
    )
    
    ]
)