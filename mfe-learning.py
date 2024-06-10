from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["learning"] = {
        "repository": "https://github.com/ejklock/frontend-app-learning.git",
        "port": 2000,
        "version": "ufmtemrede/quince.master"
    }
    return mfes
