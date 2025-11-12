import os
from pathlib import Path
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.node_parser import SentenceSplitter,TokenTextSplitter
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.DEBUG)

    
def main():
    # 作业的入口写在这里。你可以就写这个文件，或者扩展多个文件，但是执行入口留在这里。
    # 在根目录可以通过python -m chunking_research.main 运行
    load_dotenv()

    # loading
    doc_path = Path(__file__).parent.parent / "text_docs"
    documents = SimpleDirectoryReader(str(doc_path)).load_data()
    

    splitter = TokenTextSplitter(
        chunk_size=512,
        chunk_overlap=20,
        separator=" ",
    )
    nodes = splitter.get_nodes_from_documents(documents)

    # node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    # nodes = node_parser.get_nodes_from_documents(
    #     documents, show_progress=False
    # )
    for i, node in enumerate(nodes):
        logging.info(f"Chunk {i+1} (完整内容):\n{node.text}\n{'-'*50}")  # 无省略号

    # indexing
    embed_model = OpenAIEmbedding(
        model_name=os.getenv("DOUBAO_EMBEDDINGS_MODEL"),
        api_base=os.getenv("DOUBAO_API_BASE"),
        api_key=os.getenv("DOUBAO_API_KEY"),
    )
    index = VectorStoreIndex.from_documents(nodes, embed_model=embed_model)

    # queryengine
    llm_model = OpenAILike(
        model=os.getenv("DOUBAO_REASONING_MODEL"),
        api_base=os.getenv("DOUBAO_API_BASE"),
        api_key=os.getenv("DOUBAO_API_KEY"),
        is_chat_model=True
    )
    query_engine = index.as_query_engine(
        llm=llm_model, 
        streaming=False
    )

    # querying
    response = query_engine.query("小麦啤酒的主要原料是什么")
    print(response)

if __name__ == "__main__":
    main()