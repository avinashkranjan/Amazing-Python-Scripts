import os
import torch
import torchvision.transforms as transforms
from PIL import Image

model = torch.hub.load('pytorch/vision', 'deeplabv3_resnet50', pretrained=True)
model.eval()


def load_and_preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                             0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image).unsqueeze(0)
    return input_tensor


def remove_background(image_path, save_path, alpha_foreground=255, alpha_background=0):
    input_tensor = load_and_preprocess_image(image_path)

    with torch.no_grad():
        output = model(input_tensor)['out'][0]
        output_predictions = output.argmax(0)

    # Convert the prediction to a binary mask (0 for background, 1 for foreground)
    mask = output_predictions.byte()

    # Convert the mask tensor to a PIL Image with mode 'L' (8-bit pixels, black and white)
    mask_pil = transforms.ToPILImage()(mask)

    # Load the image outside the if block
    image = Image.open(image_path).convert('RGBA')

    # Resize the mask to match the dimensions of the image
    mask_pil = mask_pil.resize((image.size[0], image.size[1]))

    # Apply the mask to the input image
    image_with_alpha = Image.alpha_composite(
        Image.new('RGBA', image.size, (255, 255, 255, alpha_background)), image)
    image_with_alpha.putalpha(mask_pil.point(
        lambda p: alpha_foreground if p else 0))

    # Save the resulting image with transparent background
    image_with_alpha.save(save_path, format='PNG')


if __name__ == "__main__":
    # Replace 'input_folder' with the path to the folder containing your input images
    input_folder = "/config/workspace/project/img"

    # Replace 'output_folder' with the path where you want to save the output images
    output_folder = "/config/workspace/project/out_img"

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".avif"):
            image_path = os.path.join(input_folder, filename)
            save_path = os.path.join(output_folder, filename.replace(
                ".jpg", ".png").replace(".png", ".png"))
            remove_background(image_path, save_path)
