Python script that renders LaTeX files from LaTeX templates and YAML configs.

# Setup

Python dependencies are in `requirements.txt`. Install them with `pip` or `pip3`:

```python
pip3 install -r requirements.txt
```

The Python script creates a LaTeX file. To generate PDF from the resulting LaTeX file, install a [TeX distribution](https://www.latex-project.org/).

# Usage

| Long Arg | Short Arg | Description                                            |
|----------|-----------|--------------------------------------------------------|
| yaml     | y         | YAML config file.                                      |
| template | t         | Jinja2 LaTeX template. Located in templates directory. |
| output   | o         | LaTeX file to render.                                  |

Render a LaTeX file by running the Python script:
On Unix-like systems with Python 3 installed in `/user/bin/python3`:

```bash
./render.py -y resume.yaml -t resume.tex -o resume.tex
```

Then, generate a PDF with your TeX distribution:

```bash
xelatex resume.tex
```