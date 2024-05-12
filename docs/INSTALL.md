## Setup

Clone/Fork the repository. This project currently uses [PDM](https://pdm-project.org/en/latest/) for dependency management. 

### Instructions:

1. Initialize repository using `pdm install`
2. Update dependencies using `pdm update`
3. Activate virtual environment using `pdm venv activate`

If you do not plan to make any changes to the dependencies, you can use `pip` to install the dependencies instead.
```bash
# pip
pip install -r requirements.txt
```



### Scripts

Additional scripts are also available and can be seen using `pdm run --list`

- `start` - Start the project (run main file)
- `test` - Run tests
- `lint` - Run static analysis
- `lint-fix` - Run static analysis and fix code
- `format` - Format code
- `format-test` - Dry run for code formatting
Run at root of repository:






