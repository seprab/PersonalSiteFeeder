# PersonalSiteFeeder

This is the entry point for maintaining my personal site. I am using [Pelican](https://getpelican.com/) which is good for using markdown files as the source of every entry in my site.

Also, worth mentioning that the original source of the theme is [BT3-Flat](https://github.com/KenMercusLai/BT3-Flat) by [KenMercusLai](https://github.com/KenMercusLai/). 

## How to clone?
1. git clone --recurse-submodules git@github.com:seprab/PersonalSiteFeeder.git

## How to configure a computer to use it?
1. python -m pip install "pelican[markdown]"

## How to make new post?
> from the directory where this repo is cloned
1. Create a new .md file inside the content directory. When created inside content/static/ the post will be available as a new tab in the site. Otherwise, it will become a blog entry.
2. python -m pelican content
3. python -m pelican --listen
4. Go to http://127.0.0.1:8000 for pre-visualizing the site
4. When done with testing:
    1. Commit the changes from the submodule.
    2. Commit the changes from the parent repro


> Additional note: I created the baner in Microsoft Bing : Image creator powered by Dall-E with the prompt "peaceful indoor plants rocks daylight light beams bush lens distortion"