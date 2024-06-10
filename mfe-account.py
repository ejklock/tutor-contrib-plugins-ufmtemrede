from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["account"] = {
        "repository": "https://github.com/ejklock/frontend-app-account.git",
        "port": 1997,
        "version": "ufmtemrede/quince.3"
    }
    return mfes
