# Homebrew-formula-bump

The BumpIt script makes use of `brew livecheck` and `brew bump-formula-pr` to check for new version of formulas and PR the version bumps to Homebrew Core repo.

Warning: The script may take a long time to complete execution.

## Usage

Run the script using

```bash
python BumpIt.py
```

This will print the bump-pr statements to a bash script and to execute use

```bash
bash <date>_script.sh
```

Although it is possible to directly send the PRs from within the BumpIt script(simply uncomment the last line in the script), it is reccomended that you print to terminal or file and examine before executing as livecheck might sometimees return versions that are unstable releases or pre-releases.

### Updating the cask list

Update homebrew using `brew update` then run the updater script using

```bash
python formulalistupdater.py
```

