# SMS Spam Classification Project

## Overview

This project is part of the CodSoft internship program and focuses on building a machine learning model to classify SMS messages as spam or not spam.

## Objectives

- Develop a robust SMS spam classifier.
- Utilize various machine learning algorithms.
- Evaluate the performance of the models.

## Dataset

The dataset used for this project contains SMS messages labeled as 'spam' or 'ham' (not spam). It includes the following columns:
- `label`: The classification of the message (spam or ham).
- `message`: The content of the SMS message.

## Project Structure

- `spam_detection.py`: Main script to run the spam Classification.
- `test_messages.txt`: File containing test text for the project.
- `spam.csv`: Dataset containing spam messages or not spam messages.
- `requirements.txt`: File containing the required dependencies for the project.

## Methodology

1. **Data Preprocessing**: 
    - Cleaning and tokenizing text data.
    - Removing stop words and punctuation.
    - Converting text to numerical features using techniques like TF-IDF.

2. **Model Training**:
    - Implementing various machine learning algorithms such as Naive Bayes, SVM, and Random Forest.
    - Training models on the preprocessed dataset.

3. **Model Evaluation**:
    - Evaluating models using metrics like accuracy, precision, recall, and F1-score.
    - Comparing the performance of different models.

## Results

- The best-performing model achieved an accuracy of 95.6%.
- Detailed evaluation metrics for each model are provided in the results section.

## Conclusion

The project successfully developed a machine learning model capable of classifying SMS messages as spam or not spam with high accuracy. Future work includes improving the model's performance and exploring deep learning techniques.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/sms_spam_classifier.git
    ```
2. Navigate to the project directory:
    ```sh
    cd sms_spam_classifier
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To train and evaluate the model, run:
```sh
streamlit run spam_detetion.py
```

## License

This project is licensed under the MIT License.

## Acknowledgements

- CodSoft for the internship opportunity.
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection) for the dataset.

## License

This project is licensed under the MIT License. See the [license.md](./license.md) file for details.

## Contact

For any questions or inquiries, please contact me at:
- Name: Priyansh Jain
- Email: priyanshj839@gmail.com
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/Priyansh-Jain-India)

Feel free to reach out if you have any questions or need further information about the project.

### Libraries Used

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **NLTK**: For natural language processing tasks.
- **Scikit-learn**: For machine learning algorithms and model evaluation.
- **Matplotlib/Seaborn**: For data visualization.
- **Imbalanced-learn**: For handling imbalanced datasets.
