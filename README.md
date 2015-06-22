hdm-web-sticker-parser
=======

This module downloads and parses the sticker metadata
and creates a javascript file which can be imported to
the web project.

## Installation

1. Clone the repository

  ```sh
  git clone git@github.com:vmm/web-sticker-parser.git
  ```

2. Install dependencies

  ```sh
  npm install -g gulp
  npm install
  ```

3. Run the default task which will download the metadata files under /download directory and create the javascript module

  ```sh
  gulp
  ```

## Directory structure

/bin
 - a python script which reads the downloaded metadata and creates the javascript file

/dist
 - compiled module javascript

/downloads
 - folder where the sticker data gets downloaded
 
/src
 - pre compiled javascript