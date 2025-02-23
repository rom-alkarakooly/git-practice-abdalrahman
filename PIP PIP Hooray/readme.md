# PIP PIP Hooray

This project visualizes global population density using an interactive 3D rotating globe. The script downloads country shapefiles, calculates population density on a logarithmic scale, and renders the data using Plotly.

To set up the project, I created a virtual environment and installed the necessary dependencies manually. After confirming the script ran successfully, I generated all_requirements.txt using pip freeze and refined it into a minimal requirements.txt using pipdeptree and pipreqs.

To verify dependency management, I uninstalled all packages and confirmed that running the script resulted in an import error. I then reinstalled dependencies from requirements.txt and ensured the script functioned correctly. Finally, I used pipdeptree to analyze dependencies and documented the setup process.

The interactive globe displayed as expected, and everything worked correctly after reinstalling dependencies.

