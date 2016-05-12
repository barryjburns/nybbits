#!/bin/bash


cat << EOF
@font-face {
  font-family: "$1";
  font-weight: normal;
  font-style: normal;
  src: local("$1"),
    url("$1.ttf" format('truetype'),
    url("$1.eot" format('embedded-opentype'),
    url("$1.woff" format('woff'),
    url("$1.woff2" format('woff2'),
    url("$1.svg#$1" format('svg');
}
EOF


