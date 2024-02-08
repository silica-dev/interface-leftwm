#!/bin/sh

updates=$(apt list --upgradable 2> /dev/null | grep -c upgradable);

if [ "$updates" -gt 0 ]; then
    echo "󰚰 %{F#e0dbd4} $updates %{F-}"
else
    echo "󰸡"
fi
