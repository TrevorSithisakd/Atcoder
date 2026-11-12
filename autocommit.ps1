# Commits any changes in this repo with a timestamp. Pushes too if a remote is set.
Set-Location -Path $PSScriptRoot
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Auto-commit $(Get-Date -Format 'yyyy-MM-dd HH:mm')" | Out-Null
    if (git remote) { git push --quiet 2>$null }
}
