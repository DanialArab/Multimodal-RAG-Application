import os
import shutil
import base64

def save_extracted_elements(pdf_elements, base_dir):
    os.makedirs(os.path.join(base_dir, 'text'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'tables'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'images'), exist_ok=True)

    category_counts = {}
    items = []
    
    idx = 0
    i = 0
    while i < len(pdf_elements):
        element = pdf_elements[i]
        category = element.__class__.__name__.lower()
        category_counts[category] = category_counts.get(category, 0) + 1
        count = category_counts[category]

        # Group title/section headers with their following text block
        if category in ['title', 'sectionheader', 'header']:
            combined_text = element.text or ""
            i += 1
            # Gather following text items
            while i < len(pdf_elements):
                next_el = pdf_elements[i]
                next_cat = next_el.__class__.__name__.lower()
                if next_cat in ['text', 'paragraph', 'narrativetext', 'listitem']:
                    combined_text += "\n" + (next_el.text or "")
                    i += 1
                else:
                    break

            if combined_text.strip():
                text_path = os.path.join(base_dir, 'text', f"text_{idx}.txt")
                with open(text_path, "w", encoding="utf-8") as f:
                    f.write(combined_text)
                items.append({"type": "text", "text": combined_text, "path": text_path})
                idx += 1

        elif 'table' in category:
            try:
                if hasattr(element, "to_dataframe"):
                    table_data = element.to_dataframe()
                    table_path = os.path.join(base_dir, 'tables', f"table_{count}.csv")
                    table_data.to_csv(table_path, index=False)
                    items.append({"type": "table", "text": table_data.to_string(), "path": table_path})
                elif hasattr(element, "text"):
                    table_path = os.path.join(base_dir, 'tables', f"table_{count}.txt")
                    with open(table_path, "w", encoding="utf-8") as f:
                        f.write(element.text)
                    items.append({"type": "table", "text": element.text, "path": table_path})
            except Exception as e:
                print(f"Failed to save table {count}: {e}")
            i += 1

        elif category in ['text', 'paragraph', 'narrativetext', 'listitem']:
            try:
                text_data = element.text
                if text_data and len(text_data.strip()) > 0:
                    text_path = os.path.join(base_dir, 'text', f"text_{idx}.txt")
                    with open(text_path, "w", encoding="utf-8") as f:
                        f.write(text_data)
                    items.append({"type": "text", "text": text_data, "path": text_path})
                    idx += 1
            except Exception as e:
                print(f"Failed to save text element at index {i}: {e}")
            i += 1

        elif 'image' in category:
            try:
                metadata_dict = element.metadata.to_dict()
                image_path = metadata_dict.get("image_path")
                if image_path and os.path.exists(image_path):
                    dest_path = os.path.join(base_dir, "images", f"image_{count}.jpg")
                    shutil.copy(image_path, dest_path)
                    with open(dest_path, 'rb') as f:
                        encoded_image = base64.b64encode(f.read()).decode('utf8')
                    items.append({"type": "image", "path": dest_path, "image": encoded_image})
                else:
                    print(f"Image path missing or invalid for image {count}")
            except Exception as e:
                print(f"Failed to copy image {count}: {e}")
            i += 1

        else:
            # Skip unknown types
            i += 1

    return category_counts, items


# def save_extracted_elements(pdf_elements, base_dir):
#     os.makedirs(os.path.join(base_dir, 'text'), exist_ok=True)
#     os.makedirs(os.path.join(base_dir, 'tables'), exist_ok=True)
#     os.makedirs(os.path.join(base_dir, 'images'), exist_ok=True)

#     category_counts = {}
#     items = []

#     for idx, element in enumerate(pdf_elements):
#         category = element.__class__.__name__.lower()
#         category_counts[category] = category_counts.get(category, 0) + 1
#         count = category_counts[category]

#         if 'table' in category:
#             try:
#                 if hasattr(element, "to_dataframe"):
#                     df = element.to_dataframe()
#                     path = os.path.join(base_dir, 'tables', f"table_{count}.csv")
#                     df.to_csv(path, index=False)
#                     items.append({"type": "table", "text": df.to_string(), "path": path})
#                 elif hasattr(element, "text"):
#                     path = os.path.join(base_dir, 'tables', f"table_{count}.txt")
#                     with open(path, "w", encoding="utf-8") as f:
#                         f.write(element.text)
#                     items.append({"type": "table", "text": element.text, "path": path})
#             except Exception as e:
#                 print(f"Failed to save table {count}: {e}")

#         elif 'text' in category or 'title' in category or 'listitem' in category:
#             try:
#                 text = element.text
#                 if text and len(text.strip()) > 0:
#                     path = os.path.join(base_dir, 'text', f"text_{idx}.txt")
#                     with open(path, "w", encoding="utf-8") as f:
#                         f.write(text)
#                     items.append({"type": "text", "text": text, "path": path})
#             except Exception as e:
#                 print(f"Failed to save text {idx}: {e}")

#         elif 'image' in category:
#             try:
#                 metadata = element.metadata.to_dict()
#                 image_path = metadata.get("image_path")
#                 if image_path and os.path.exists(image_path):
#                     dest_path = os.path.join(base_dir, "images", f"image_{count}.jpg")
#                     shutil.copy(image_path, dest_path)
#                     with open(dest_path, 'rb') as f:
#                         encoded_image = base64.b64encode(f.read()).decode('utf8')
#                     items.append({"type": "image", "path": dest_path, "image": encoded_image})
#             except Exception as e:
#                 print(f"Failed to copy image {count}: {e}")

#     return category_counts, items
