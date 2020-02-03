Jiml is a Python script that renders Jinja templates with data from YAML files.

This allows users to maintain one YAML file of data that can be published into many other formats.
For example, a CV can be maintained in a single YAML file but published as HTML and LaTeX.

# Usage

| Long Arg | Short Arg | Description             |
|----------|-----------|-------------------------|
| yaml     | y         | YAML config file.       |
| template | t         | Jinja2 LaTeX template.  |
| output   | o         | Output file to render.  |

On Unix-like systems with Python 3 installed in `/user/bin/python3`:

```bash
./render.py -y demo.yaml -t tech-resume.tex -o demo-resume.tex
```

If you want to generate a PDF from a [LaTeX](https://www.latex-project.org/) file:

```bash
xelatex demo-resume.tex
```

## Supported Output

By default, YAML data is escaped depending on the output format.
Jiml supports for the following formats for escaping:

- LaTeX
- HTML
- XML


You can render plaintext file formats not in the list above, but special characters will not be escaped.

# Development

Python dependencies are in `requirements.txt`. Install them with `pip` or `pip3`:

```python
pip3 install -r requirements.txt
```

Git hooks live in `.githooks`. For git clients older than version `2.9`, set this as your `hooksPath`:

```bash
git config core.hooksPath ".githooks"
```