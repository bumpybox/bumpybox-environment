import os

import Deadline.Scripting as ds


def __main__(jobId):
    job = ds.RepositoryUtils.GetJob(jobId, True)

    if os.path.exists(job.GetJobPluginInfoKeyValue("SceneFile")):
        return True

    return False
