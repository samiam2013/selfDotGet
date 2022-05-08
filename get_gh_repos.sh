#!/bin/bash
curl -i -u samiam2013:$github_token https://api.github.com/user/repos > $(date +%s).repos.json

