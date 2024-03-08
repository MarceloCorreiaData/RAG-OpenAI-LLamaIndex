# RAG-OpenAI-LLamaIndex
RAG Vector Store using Open Soucer and OpenAI LLMs on LlamaIndex Langchain. \
It comprehends the creation of a new Reader Class.

The HierarchicalJSONReader class, derived from BaseReader, is designed to parse JSON files, including both dictionaries and lists of concatenated JSON dictionaries. It constructs a hierarchical document structure that mirrors the JSON tree, translating the key-value pairs (and lists) into a structured format. This structure is organized into root nodes, branch nodes, and leaf nodes, which are categorized as categories and subcategories within the documents. The class facilitates the extraction of complex relationships and metadata from JSON documents, enabling detailed analysis and representation of the data in accordance with its inherent hierarchical organization.

Furthermore, the HierarchicalJSONReader is equipped with features that enhance its ability to manage and interpret complex JSON structures. These include configurable parameters such as levels_back, which determines the depth of hierarchy to be considered, and collapse_length, allowing for the condensation of JSON fragments into a single line based on character count limits. This flexibility makes it adept at handling various data sizes and complexity, from simple key-value pairs to deeply nested JSON objects.

Additionally, the class supports JSONL format, enabling efficient processing of large datasets commonly found in machine learning and data analysis projects. By providing detailed control over how data is parsed and structured, the HierarchicalJSONReader opens up possibilities for nuanced data exploration, making it an invaluable tool for developers and data scientists looking to leverage hierarchical information within JSON files for advanced analytics and machine learning models.

