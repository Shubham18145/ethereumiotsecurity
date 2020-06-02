classification/ directory contains files needed for preprocessing and sampling of dataset and then applying machine learning models.

Source of dataset: (Reference: http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones)


It contains following python files: 

1. Preprocess_Dataset.py _ It contains logic to preprocess, clean the dataset and convert data in .txt format to .csv format. Then it does sampling after meging test and train datasets to pick subset of dataset to be used as an input to Ethereum blockchain.  

2. Process_dataset_from_Blockchain.py - It contains logic to retrieve dataset from Ethereum and run machine learning algorithms (Naive Bayes, Random Forest and SVM) in order to calculate accuracy, recall, MCC.

3. Process_tampered_dataset.py - It contains logic to tamper original dataset and run machine learning algorithms (Naive Bayes, Random Forest and SVM) in order to calculate accuracy, recall, MCC.


Classes in our classification problem - Labels 1,4,5,6 (where labels 1,2,3 are merged as they denote activities similar to WALKING)


Steps to run:

1. Generate "preprocessed_data_to_blockchain.txt" by running Preprocess_Dataset.py

2. Run following script to copy particular row from dataset (each row is present in each line of txt file) 
    sh copy_to_browser.sh preprocessed_data_to_blockchain.txt <line_number>
    
    This copies one row from txt file to clipboard. Paste it to Enter data field in frontend.
    Click on Submit to insert data into smart contract deployed on Ropsten testnet.
    Repeat it (running shell script) for every line number. Insert transaction will take some time to run. Please enter data one by one.
    
3. After multiple rows have been inserted into Ropsten testnet, click on Submit below Read Data. Click again to sort in ascending order via ID.
   Click on Copy text to copy whole dataset retrieved from Ropsten testnet. Paste it in "data_retrieved_from_blockchain.txt".
   
4. Run Process_dataset_from_Blockchain.py and Process_tampered_dataset to get results in terms of accuracy, recall and MCC for both cases. 
   (Result may vary based on sampling and seed)
