#!/usr/bin/env python
import os
import webbrowser

dir_path = os.getcwd()
github_config = open(dir_path + "/.git/config", "r")
gc_lines = github_config.readlines()
url = ''

# Extract url from config file
for x in range(0, len(gc_lines)):
  if x == 8:
    url = gc_lines[x]

# Extract url from string
parsed_url = url.strip().split('@')[1].replace(":", "/").replace(".git", "")
final_url = "https://" + parsed_url

# Open url in a new page (“tab”) of the default browser, if possible
webbrowser.open_new_tab(final_url)