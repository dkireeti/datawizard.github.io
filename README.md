# DataWizard
One place for ML Learning Simplified

This repository hosts course materials for DataWizard: short notebooks and pages aimed at teaching machine learning from first principles.

Getting started (local)

Install the build dependencies and create the HTML site locally with Jupyter Book:

```bash
pip install -r requirements.txt
# Build the HTML site (explicitly select the HTML builder/export):
jupyter-book build . --builder html --site
```

The built site will be placed under `_build/html` by default. We'll add a CI workflow to publish the site to `docs/` for GitHub Pages in a later step.

See `Carriculum.md` for the course outline and `content/python-basics.md` + `notebooks/python_basics.ipynb` for the first lesson.