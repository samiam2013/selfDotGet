#!/bin/bash

# this request downloads an example of the request result used to downlaod all the repositories for the user
curl -i -u $GITHUB_USER:$GITHUB_TOKEN https://api.github.com/user/repos > $(date +%s).repos.json

