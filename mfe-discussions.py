from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["discussions"] = {
        "repository": "https://github.com/ejklock/frontend-app-discussions.git",
        "port": 2002,
        "version": "ufmtemrede/quince.indigo"
    }
    return mfes
