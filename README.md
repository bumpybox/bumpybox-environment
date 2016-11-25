# bumpybox-core
The centralized pipeline used at Bumpybox.

**Dependencies**

This package depends on https://github.com/tokejepsen/conda-git-deployment.
Download/Clone and add the following ```environment.yml```:

```yaml
name: bumpybox-core
dependencies:
   - git:
     - "https://github.com/Bumpybox/bumpybox-core.git":
        - "python $REPO_PATH/startup.py"
```
