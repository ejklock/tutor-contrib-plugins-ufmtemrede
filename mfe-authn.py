from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["authn"] = {
        "repository": "https://github.com/ejklock/frontend-app-authn.git",
        "port": 1999,
        "version": "ufmtemrede/quince"
    }
    return mfes
