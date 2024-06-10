from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["learning"] = {
        "repository": "https://github.com/ejklock/frontend-app-ora-grading.git",
        "port": 1993,
        "version": "ufmtemrede/quince.3"
    }
    return mfes
