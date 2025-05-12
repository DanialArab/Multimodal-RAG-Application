import os
import shutil
import base64

def save_extracted_elements(pdf_elements, base_dir):
    os.makedirs(os.path.join(base_dir, 'text'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'tables'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'images'), exist_ok=True)

    category_counts = {}
    items = []

    for idx, element in enumerate(pdf_elements):
        category = element.__class__.__name__.lower()
        category_counts[category] = category_counts.get(category, 0) + 1
        count = category_counts[category]

        if 'table' in category:
            try:
                if hasattr(element, "to_dataframe"):
                    df = element.to_dataframe()
                    path = os.path.join(base_dir, 'tables', f"table_{count}.csv")
                    df.to_csv(path, index=False)
                    items.append({"type": "table", "text": df.to_string(), "path": path})
                elif hasattr(element, "text"):
                    path = os.path.join(base_dir, 'tables', f"table_{count}.txt")
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(element.text)
                    items.append({"type": "table", "text": element.text, "path": path})
            except Exception as e:
                print(f"Failed to save table {count}: {e}")

        elif 'text' in category or 'title' in category or 'listitem' in category:
            try:
                text = element.text
                if text and len(text.strip()) > 0:
                    path = os.path.join(base_dir, 'text', f"text_{idx}.txt")
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(text)
                    items.append({"type": "text", "text": text, "path": path})
            except Exception as e:
                print(f"Failed to save text {idx}: {e}")

        elif 'image' in category:
            try:
                metadata = element.metadata.to_dict()
                image_path = metadata.get("image_path")
                if image_path and os.path.exists(image_path):
                    dest_path = os.path.join(base_dir, "images", f"image_{count}.jpg")
                    shutil.copy(image_path, dest_path)
                    with open(dest_path, 'rb') as f:
                        encoded_image = base64.b64encode(f.read()).decode('utf8')
                    items.append({"type": "image", "path": dest_path, "image": encoded_image})
            except Exception as e:
                print(f"Failed to copy image {count}: {e}")

    return category_counts, items
