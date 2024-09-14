## Yandex Disk Mirror App

You can test this app here - https://13.60.250.255/

[Screencast from 2024-09-15 01-39-42.webm](https://github.com/user-attachments/assets/1af30d3c-af7c-4798-ad1c-0036dff8675b)

## Installation

### Python 3.12.3

1. Create and activate a virtual enviroment

2. Install libs from `requirements.txt`

3. Run `main.py`

4. App will be available at the address provided in `config.py`

## Usage

To test an application, login to default user. Login - `admin`, Password - `12345678`. Then, Paste to the search bar link to publicly available yandex disk. It might be a full link - `https://disk.yandex.ru/d/coIIrxEva7kPoQ` or just a public key - `coIIrxEva7kPoQ`. Press `search` button to get data from disk on website. By clicking on elemenets, you can navigate via folders (back and forth) and download files.

## Task:

Create a web application using Flask or Django that interacts with the Yandex.Disk API.

The application should implement the following functionality:

1. Viewing files on Yandex.Disk using a public link (public_key):
   After successful authorization, the user should be able to see a list of all files and folders stored under the provided public link.

2. Downloading specific files:
   The user should be able to select files from the list and download them to their local computer via the web application's interface.

## Technical requirements:

- Use Flask or Django as the web framework.

- Fetch the list of files from Yandex.Disk using the REST API.

- Implement the ability to download selected files from Yandex.Disk to the local computer.

- The application should have a simple web interface to display the list of files and provide buttons for downloading them.

## Additional requirements:

- You can use the `requests`/`aiohttp` library or any other HTTP client library to work with the Yandex.Disk API.

- Document the code, including type annotations.

- The code should be uploaded to GitHub or a similar service with a commit history.

## Evaluation criteria:

- Correct implementation of authorization and API interaction.

- Usability and simplicity of the interface.

- Readability and structure of the code.

- The presence of instructions for launching and using the application.

- Compliance with the technical and additional requirements of the task.

## Optional tasks (not mandatory, but would be a plus):

1. Implement file filtering by type (e.g., documents only or images only).

2. Allow downloading multiple files simultaneously.

3. Implement caching of the file list so that it doesn’t have to be fetched from the server each time.
