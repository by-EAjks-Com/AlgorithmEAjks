# AlgorithmEAjks Package

## Instructions

### On the LocalHost

```powershell
docker run `
    --interactive `
    --tty `
    --gpus all `
    --name algorithmeajks `
    --publish 8888:8888 `
    --volume "/Path/To/AlgorithmEAjks/Code:/src" `
    --workdir /build `
    docker.io/eajkseajks/python-algorithmeajks:v1-ubuntu-22.04-latest
```

```powershell
docker start --interactive algorithmeajks
```

### In the Container

```bash
cd /build
. ./.venv/bin/activate
```

#### Develop & Test

```bash
cd /src/Algorithms/AlgorithmEAjks
pip install --editable .
pytest
py3clean .
```

```bash
cd /src/Algorithms/AlgorithmEAjks
tox
```

#### Build & Install

```bash
cd /src/Algorithms/AlgorithmEAjks
python -m build --sdist
python -m build --wheel
python -m build
pip install dist/algorithmeajks-0.0.1-py3-none-any.whl
py3clean .
```

#### Launch Jupyter Lab

```bash
jupyter-lab --allow-root --ip=0.0.0.0 --no-browser /src
```

## References

- <https://python-yahoofinance.readthedocs.io/en/latest/api.html>
