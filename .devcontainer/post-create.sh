#!/usr/bin/env bash
set -euo pipefail

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
eval "$(pyenv init -)"

echo "python: $(python --version)  (pyenv $(pyenv global))"
echo "installed interpreters: $(pyenv versions --bare | tr '\n' ' ')"

if [ -f requirements.txt ]; then
  pip install --no-cache-dir -r requirements.txt
fi

if [ -f pyproject.toml ] && grep -q '\[tool.poetry\]' pyproject.toml; then
  poetry install
fi

cat <<'EOF'

Ready. This interpreter is 3.12 (modern). To work against an old Python:
  pyenv install 2.7.18        # or 3.6.15, 3.8.18, etc.
  pyenv local 2.7.18          # pins this version for the current directory
  pyenv versions              # list what's installed
EOF
