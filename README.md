# link-navi

Python module for extracting hyperlinks from strings.
Also gathers additional metadata for links (e.g. if its a youtube video: video statistics and channel name).

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