from unstructured.partition.pdf import partition_pdf

def extract_pdf_elements(filename):
    return partition_pdf(
        filename=filename,
        extract_images_in_pdf=True,
        strategy="hi_res",
        hi_res_model_name="yolox",
        infer_table_structure=True,
        max_characters=3000,
        combine_text_under_n_chars=200,
    )


