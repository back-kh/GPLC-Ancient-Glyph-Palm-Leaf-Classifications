from preprocessing.data_preprocessing import load_data, create_data_generators
from models.efficientnet_model import build_efficientnet_model
from models.resnet_model import build_resnet_model
from models.cvt_model import build_vit_model, build_cvt_model
from models.swin_model import build_swin_model
from training import train_and_evaluate
from utils import plot_samples

def main(model_type='efficientnet'):
    # Load data
    df_train, df_test = load_data()
    train_gen, valid_gen, target_dict = create_data_generators(df_train, df_test)

    # Show sample images
    plot_samples(train_gen)

    # Build and train the model
    if model_type == 'efficientnet':
        model = build_efficientnet_model(num_classes=len(target_dict))
    elif model_type == 'resnet':
        model = build_resnet_model(num_classes=len(target_dict))
    elif model_type == 'vit':
        model = build_vit_model(num_classes=len(target_dict))
    elif model_type == 'cvt':
        model = build_cvt_model(num_classes=len(target_dict))
    elif model_type == 'swin':
        model = build_swin_model(num_classes=len(target_dict))
    else:
        raise ValueError("Invalid model type specified!")

    train_and_evaluate(model, train_gen, valid_gen)

if __name__ == "__main__":
    main(model_type='efficientnet')  # Change to 'resnet', 'vit', 'cvt', or 'swin' as needed
