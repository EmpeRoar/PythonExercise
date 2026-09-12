FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

ARG PYTHON_VERSION=3.12.6

# Build dependencies needed by pyenv to compile any CPython version (old or new)
# from source: https://github.com/pyenv/pyenv/wiki#suggested-build-environment
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        libncursesw5-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libffi-dev \
        liblzma-dev \
        uuid-dev \
        tk-dev \
        xz-utils \
        curl \
        git \
        llvm \
        wget \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER vscode
ENV PYENV_ROOT="/home/vscode/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"

# pyenv + pyenv-virtualenv, so old interpreters (2.7, 3.6, ...) can be
# installed on demand later with: pyenv install <version>
RUN curl -fsSL https://pyenv.run | bash \
    && echo '' >> /home/vscode/.bashrc \
    && echo '# pyenv' >> /home/vscode/.bashrc \
    && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /home/vscode/.bashrc \
    && echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/vscode/.bashrc \
    && echo 'eval "$(pyenv init -)"' >> /home/vscode/.bashrc \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vscode/.bashrc \
    && cp /home/vscode/.bashrc /home/vscode/.zshrc 2>/dev/null || true

# Bake in one modern interpreter so the container is usable immediately;
# everything older is a one-line `pyenv install <version>` away.
# (pyenv's subcommands only need $PYENV_ROOT/bin on PATH, already set above.)
RUN pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    && pyenv rehash

ENV PATH="$PYENV_ROOT/shims:$PATH"

# Common dev tooling on the global (3.12) interpreter, so it's usable both
# as a CLI and via `import` without a project virtualenv.
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir ruff black mypy pytest ipython

# Poetry is a standalone tool, not a library, so it gets its own isolated
# environment via pipx (keeps it out of every project's dependency tree).
RUN pip install --no-cache-dir pipx \
    && pipx ensurepath \
    && pipx install poetry

ENV PATH="/home/vscode/.local/bin:$PATH"
