from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["profile"] = {
        "repository": "https://github.com/ejklock/frontend-app-profile.git",
        "port": 1995,
        "version": "ufmtemrede/quince.3"
    }
    return mfes
