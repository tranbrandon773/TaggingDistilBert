### 1. Data Collection and Initial Pre-processing
- We used the API to grab all of the transactions available, total of 1628.
### 2. Enhancing Data Quality and Tagging
- Only eight percent of all transactions had a pre-existing tag.
- We used an LLM to fill in the rest of the tags and manually verified them.
- We created a set of tags: ['Funding', 'Operations', 'Misc', 'Food', 'Equipment', 'Programming', 'Travel'] that will be used in subsequent analysis.
### 3. DistilBERT and Fine-tuning
We chose to use DistilBERT, a distilled version of the BERT model, for its efficiency and relatively lower computational cost while maintaining a high level of performance. DistilBERT is designed to be smaller, faster, and lighter than BERT, making it more suitable for environments with limited resources, without significantly compromising the model's ability to understand and process natural language.
- **Efficiency:** DistilBERT retains most of the original BERT model's effectiveness but is 40% smaller and 60% faster. This efficiency allows us to train and infer more quickly, which is crucial for iterating over model improvements and handling a large volume of data.
- **Performance:** Despite its reduced size, DistilBERT maintains up to 97% of BERT's performance on several benchmark tasks. This high level of performance is essential for ensuring our model accurately suggests tags for transactions.
#### Fine-tuning Process
It wsa evident that fine-tuning was in order on account of the base model's 16% accuracy (test data).
- **Dataset Preparation:** See 1 and 2.
- **Model Architecture:** Our DistilBERT model includes a pre-classification layer and a dropout layer to prevent overfitting, followed by a classification layer that maps the distilled BERT embeddings to our 7 predefined categories, see 2.
- **Training:** We fine-tuned DistilBERT on our transaction dataset with a learning rate of 1e-05 over 5 epochs.
- **Evaluation:** The model achieved an accuracy of 77.85% on the test set.
### 4. Synthetic Data Expansion and Balancing
To enhance the robustness and accuracy of our model, we significantly expanded our dataset by synthesizing additional data, resulting in a comprehensive collection of 25,000 memo-tag pairs. This expansion aimed to provide a more varied and extensive training environment for our model, addressing any potential data scarcity and diversity issues.
#### Dataset Balancing
Prior to training, we meticulously balanced the new dataset to ensure an equitable representation of each category. This step prevents the model from developing biases towards more frequently represented categories, thus improving its ability to accurately classify a wider range of inputs.
#### Model Training and Hyperparameter Optimization
Our experimentation with various hyperparameter settings led us to identify an optimal configuration of 3 epochs and a learning rate of 1e-05, achieving these results:
- **Test Data Accuracy:** 98.21%
- **Training Accuracy:** 98.81%

These outcomes underscore the significant impact of synthetic data augmentation. The process improved the model's ability to generalize across a broader dataset.

### 5. Data Visualization
Since we had the tags for all of the available transactions from the API, we went ahead and created pie charts to visualize how organizations spent the money they raised. The pie charts are titled with the organizations ID.

### 6. Considerations and Future Work
#### Considerations
- While the synthetic data expansion and balancing have improved model performance, ongoing efforts are required to monitor and mitigate any biases that may emerge, especially as new categories or data sources are introduced.
- As the dataset grows with more transactions, maintaining model performance and efficiency will be crucial.
#### Future Work
- Developing a system that can adapt to new categories of spending as they emerge, allowing for more granular insights into organizational spending patterns.
- Implementing a feedback loop from users to continually refine the tagging accuracy and relevance, potentially using active learning to prioritize uncertain cases for human review.
- Evaluating the model using F1 score, studying the confusion matrix, etc. 