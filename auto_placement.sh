#!/bin/bash

MODE_RUN="run"
MODE_BACKUP="backup"
MODE_REPAIR="repair"
MODES=($MODE_RUN $MODE_BACKUP $MODE_REPAIR)

. ./dir_conf.txt

usage() {
    echo -e """Usage: auto_placement.sh MODE

    MODE: ${MODES[@]}
    """
}

if [ 1 -ne $# ]; then
    usage
    exit 1
fi

if ! `echo ${MODES[@]} | grep -wq "$1"` ; then
    usage
    exit 1
fi

MODE=$1

backup() {
    if [ ! -e $BACKUP_DIR ]; then
        mkdir $BACKUP_DIR
    fi
    if [ -e $INDEX_DIR/$INDEX_NAME ]; then
        sudo cp -i $INDEX_DIR/$INDEX_NAME $BACKUP_DIR
    fi
    if [ -e $CONFIG_DIR/$CONFIG_NAME ]; then
        sudo cp -i $CONFIG_DIR/$CONFIG_NAME $BACKUP_DIR
    fi
    if [ -e $MAIN_CODE_DIR/$MAIN_CODE_NAME ]; then
        sudo cp -i $MAIN_CODE_DIR/$MAIN_CODE_NAME $BACKUP_DIR
    fi
}

repair(){
    if [ -e $BACKUP_DIR ]; then
        sudo cp $BACKUP_DIR/$INDEX_NAME $INDEX_DIR
        sudo cp $BACKUP_DIR/$CONFIG_NAME $CONFIG_DIR
        sudo cp $BACKUP_DIR/$MAIN_CODE_NAME $MAIN_CODE_DIR
    else
        echo "Backup Directory cannot be found."
    fi
}

run(){
    backup
    sudo cp $ITEMS_DIR/$INDEX_NAME $INDEX_DIR/$INDEX_NAME
    sudo cp $ITEMS_DIR/$CONFIG_NAME $CONFIG_DIR/$CONFIG_NAME
    sudo cp $ITEMS_DIR/$MAIN_CODE_NAME $MAIN_CODE_DIR/$MAIN_CODE_NAME
}

if [ $MODE_RUN = $MODE ]; then
    run
    echo $MODE_RUN
fi

if [ $MODE_REPAIR = $MODE ]; then
    backup
    echo $MODE_REPAIR
fi

if [ $MODE_BACKUP = $MODE ]; then
    echo $MODE_BACKUP
fi
