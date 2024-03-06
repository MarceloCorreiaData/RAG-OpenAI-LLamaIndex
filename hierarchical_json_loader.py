import json
from pathlib import Path
from llama_index import download_loader

def JSONLoaderHierarchical(input_path, output_path):
    """
    Transforma um arquivo JSON, adicionando hierarquia e metadados, e carrega os documentos.

    Args:
        input_path (str): Caminho para o arquivo JSON original.
        output_path (str): Caminho para salvar o arquivo JSON transformado.

    Returns:
        documents: "LlamaIndex Documents" carregados do arquivo JSON transformado.
    """
    with open(input_path, 'r', encoding='utf-8') as file:
        data_list = json.load(file)

    metadata_list = []
    
    for data in data_list:
        transformed_metadata = {}
        categories = []
        subcategories = []
        
        for category, contents in data.items():
            categories.append(category)
            transformed_contents = {}
            
            for subcategory, value in contents.items():
                new_subcategory = f"{category} - {subcategory}"
                subcategories.append(new_subcategory)
                transformed_contents[new_subcategory] = value
                
            transformed_metadata[category] = transformed_contents
        
        transformed_metadata["metadata"] = {
            "categories": categories,
            "subcategories": subcategories
        }
        
        metadata_list.append(transformed_metadata)

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(metadata_list, file, ensure_ascii=False, indent=4)
    
    JSONReader = download_loader("JSONReader")
    loader = JSONReader()
    documents = loader.load_data(Path(output_path))
    
    return documents
