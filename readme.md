# Description
This (mac-only) python script will take a YouTube playlist and download each video in it all at once. 
Each youtube-dl process opens in a new terminal window so you can see its progress and make sure there are no errors.

# Prerequisites:
Install python3 and youtube-dl

Only works on mac

# Instructions
Run it like: 
`python3 ytdl-simul.py playlist <playlistCode>`

The playlistCode is the code in the YouTube URL you see when you visit the playlist page. For example, if the URL is:

`https://www.youtube.com/playlist?list=PL7261909612328DAC`, the code is `PL7261909612328DAC`.

So the command would look like this:
`python3 ytdl-simul.py playlist PL7261909612328DAC`


# Tip
I recommend using a config file to specify parameters you normally enter with youtube-dl, especially an output path or this script will download them to your root path. 
The script currently doesn't pass parameters through to youtube-dl, so the config file is the only way to specify options.

An example config file is in the repo which can be placed here:
`~/.config/youtube-dl/config`