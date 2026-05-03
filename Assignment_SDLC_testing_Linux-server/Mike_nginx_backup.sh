#!/bin/bash

DATE=$(date +%y%m%d)
BACKUP_DIR="/backups"
BACKUP_FILE="$BACKUP_DIR/Mike_nginx_backup_$DATE.tar.gz"
LOG_FILE="$BACKUP_DIR/Mike_nginx_backup_log_$DATE.txt"

# Create backup path for Mike Backup if Not present

mkdir -p  $BACKUP_DIR

# Creating backup file  and storing logs in LOG_FILE

tar -czf $BACKUP_FILE /etc/nginx/ /usr/share/nginx/html/ 2>> $LOG_FILE

# Verification if Backup is get completed
echo "Backup verification for $BACKUP_FILE on $(date)" >> $LOG_FILE
tar -tzf $BACKUP_FILE >> $LOG_FILE  2>&1

# Notification once backup completed
echo "Backup completed for nginx on $(date)" >> $LOG_FILE

