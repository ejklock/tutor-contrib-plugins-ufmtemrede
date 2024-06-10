from tutormfe.hooks import MFE_APPS


@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["learner-dashboard"] = {
        "repository": "https://github.com/ejklock/frontend-app-learner-dashboard.git",
        "port": 1996,
        "version": "ufmtemrede/quince.master"
    }
    return mfes
