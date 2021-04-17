# School-Opening-Scraper

## About

This is a collection of Python scripts to scrape US K-12 school instruction modality data from government websites. Each state script pulls information either from HTML scraping or downloadable CSV/XLSX files and converts the data to a uniform CSV format. The unified data will be integrated with HHS Protect Public for public access and easy data analysis. This is a project by the Fall 2020 - Spring 2021 VSFS Interns at HHS OCIO.

The repository uses [Pipenv](https://packaging.python.org/key_projects/#pipenv) to manage package dependencies. Usage of [Python 3.9](https://www.python.org/downloads/) is recommended. Collected/produced CSV and XLSX filed are excluded from the repository.

If you have any problems or questions about this repository, please feel free to open an [issue on GitHub](https://github.com/trackman1111/School-Opening-Scraper/issues).

## Running the Scraper

1. Install [Python](https://www.python.org/downloads/)
2. Install [Pipenv](https://packaging.python.org/tutorials/managing-dependencies/#installing-pipenv)
3. Navigate to the project root directory
4. Run `pipenv install` to install the dependencies from the Pipfile
5. Run the script with `pipenv run python main.py`
   - If you get an error that `pipenv` is not available, you may need to [edit your system `PATH`](https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site)
   - You can also open a shell within this virtual environment using `pipenv shell`

## Adding a State Script

To add a script for a new state, create a file in the format `state_name.py` in the root directory. You can then use the following sample code to help you write the script:

```
#add all imports here
import requests


def main():
    download_csv()
    print("<STATE_ABBREVIATION> - Downloaded CSV")
    copy_to_new_csv()
    print("<STATE_ABBREVIATION> - Wrote CSV")


def download_csv():  # or download_xslx()
    # Dowload file locally using ("./StateNameOriginal.extension")

def copy_to_new_csv():
    # Write to School Districts

# Add more helper methods if needed

main()
```

Once you've written your program, you can run it with this command: `pipenv run python state_name.py`.
If your program is working as expected, you can add it to `main.py` by adding `import state_name` at the top and `state_name.main()` beneath the currently present states.

### Adding a Package

You can see the current list of available packages in the `Pipfile`. This includes `bs4` (Beautiful Soup for web scraping), `openpyxl` (for handling XLSX files), and `requests` (for downloading files from URLs). To add a new package, follow these steps:

1. Navigate to the project root directory
2. Run `pipenv install package_name`
3. Add an import statement to your Python file: `import package_name`
   This will add the package to the list of dependencies in the `Pipfile` and make it available to you.

### Using PyCharm

Follow [this tutorial](https://www.jetbrains.com/help/pycharm/pipenv.html) to set-up Pipenv with PyCharm for an existing Python project.
When running individual state scripts, use the `state_name.py` as the executable in the PyCharm configuration.
When running `main.py`, use that file as the executable.
