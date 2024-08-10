# Unigen

Wrapper around python's mutagen package which provides a single interface to interact with audio metadata of various formats

## Dependencies installation

For installing dependencies:
`pip install -r requirements.txt`

To add a new dependency, add it to `setup.py` and `requirements.in`. Then:

```
pip install pip-tools
pip-compile --upgrade
pip-sync
```

This will update `requirements.txt`

For publishing latest update

- Bump up `version` in `setup.py` file to `$newVersion`
- Commit the change with something like: `release: bump up version to $newVersion`
- Tag the latest commit as the latest version using `git tag $newVersion`
- push the commit to origin using `git push origin main`
- push the tag to start `publish-to-pypi` build using `git push $newVersion`

example:

```
git add setup.py
git commit -m "release: bump up version to v1.4.1"
git tag v1.4.1
git push origin main
git push v1.4.1
```

Make sure to tag after bumping up the version since tag pushes are linked to their previous commits
