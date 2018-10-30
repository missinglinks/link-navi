# link-navi

Python module for extracts hyperlinks from strings and gathers additional metadata for the link (e.g. if its a youtube video, it looks up video statistics and channel name).

Currently identifies the following links:
* Youtube
* Twitter


## Installation

Clone repository

```
$ git clone https://github.com/missinglinks/link-navi.git
```

Install module using pip

```
$ cd link-navi
$ pip install -e .
```


## Usage

```
import linknavi als ln

navi = ln.LinkNavi("youtube-api-key")
links = navi.parse("text with https://www.github.com hyperlink")

```