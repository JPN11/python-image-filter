import os
from filter import apply_filter

def test_filters(image_path):
    output_dir = 'filter/filtered_images'
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

    filters = ['grey', 'sepia', 'invert', 'blur', 'reflect', 'sharpen', 'contour', 'detail', 'edge', 'emboss']
    for filter_name in filters:
        try:
            print(f"Applying {filter_name} filter...")
            image = apply_filter(image_path, filter_name)
            output_path = os.path.join(output_dir, f"{filter_name}_filtered.jpg")
            image.save(output_path)  # Save the filtered image
            print(f"Saved {filter_name} filter image to {output_path}")
        except Exception as e:
            print(f"Error applying {filter_name} filter: {e}")

if __name__ == "__main__":
    test_image_path = 'filter/images/python.jpg'  # Path to the test image
    test_filters(test_image_path)
