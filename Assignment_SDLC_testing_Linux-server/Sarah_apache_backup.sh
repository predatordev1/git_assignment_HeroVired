#!/bin/bash

# Apache Backup Script - Sarah
# Backup Date: current date in YYYY-MM-DD format

DATE=$(date +%y%m%d)
BACKUP_DIR="/backups"
BACKUP_FILE="$BACKUP_DIR/Sarah_apache_backup_$DATE.tar.gz"
LOG_FILE="$BACKUP_DIR/Sarah_apache_backup_logs_$DATE.txt"

# Create backup path for Sarah Backup if Not present
 
mkdir -p  $BACKUP_DIR 

# Creating backup file  and storing logs in LOG_FILE

tar -czf $BACKUP_FILE /etc/httpd/ /var/www/html/ 2>> $LOG_FILE

# Verification if Backup is get completed 
echo "Backup verification for $BACKUP_FILE on $(date)" >> $LOG_FILE
tar -tzf $BACKUP_FILE >> $LOG_FILE 2>&1

# Notification once backup completed
echo "Backup completed for Apache on $(date)" >> $LOG_FILE 
