# Mechanizer Data Science

## OSDI Sync
The app will sync data from an OSDI endpoint.  The following OSDI related environment variables are used

1. OSDI_AEP: The URL to the OSDI API Endpoint that lists collections available on the server
2. OSDI_TOKEN: The OSDI-API-Token for authentification if needed
3. OSDI_BROWSER: The URL to the HAL Browser instance for the AEP.  This is for the menus, not used in sync

> See implementation in mechdata/datamover.py and mechdata/views.py

## Sentiment Analysis
Logistic regression from scikit-learn is used to determine the sentiment of text.  This is done either on:

1. Manual Entry by user
2. OSDI synchronized data

> See implementation in mechdata/stats.py and mechdata/views.py

