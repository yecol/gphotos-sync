#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ${DIR}

pipenv run ../gphotos-sync \
    ../photostream \
    --secret ./client.json \
    --album yweb \
    --use-flat-path \
    --log-level trace

grep -w yweb-token ../photostream/gphotos.log | cut -d" " -f10-12 > ../photostream/yweb_origins.txt