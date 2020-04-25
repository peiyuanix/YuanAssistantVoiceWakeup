#! /bin/bash
PROGDIR=$(dirname $(readlink -f "$0"))

if [ ! -d "$PROGDIR/audio" ]; then
    mkdir $PROGDIR/audio
fi

arecord -d 2 -r 16000 -c 1 -f S16_LE $PROGDIR/audio/voice-record.wav && /usr/bin/python $PROGDIR/asr_raw.py
