#!/bin/sh

. ./dir_conf.txt

if [ ! -e $BACKUP_DIR ]; then
    mkdir $BACKUP_DIR

    if [ -e $INDEX_DIR ]; then
       sudo cp -i $INDEX_DIR $BACKUP_DIR/
    fi
    if [ -e $CONFIG_DIR ]; then
       sudo cp -i $CONFIG_DIR $BACKUP_DIR/
    fi
    if [ -e $MAIN_CODE_DIR ]; then
       sudo cp -i $MAIN_CODE_DIR $BACKUP_DIR/
    fi
fi

echo $INDEX_DIR
