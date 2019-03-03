===========================
Some handy commands in git: Credits to stackoverflow, manuals, etc.
===========================

1. If you accidentally commited large files and can't push to github, filter it out from commit history. Don't forget to back it up:
git filter-branch --tree-filter 'rm -rf path/to/file' HEAD
git push -u origin master --force
