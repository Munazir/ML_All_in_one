import numpy as np
from config.core import configs
from sklearn.model_selection import train_test_split


# function to train the model

def run_training() -> None:
    """Train the model"""
    #TODO
    # read training data
    data = load_dataset(filename=configs.app_configs.training_data_file)

    # train test split
    X_train, X_test , y_train, y_test = train_test_split(
        x=data[configs.model_configs.features],
        y=data[configs.model_configs.target]
        test_size=configs.model_configs.test_size,
        random_state=configs.model_configs.random_state,)

    #TODO
    #fit model
    price_pipe.fit(X_train,y_train)

    # persist the model
    save_pipeline(pipeline_to_persist=price_pipe)

