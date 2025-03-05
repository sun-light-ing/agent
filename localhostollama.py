from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama

ollama_embedding = OllamaEmbedding(
    model_name="bge-m3",
    base_url="http://localhost:6006",
    ollama_additional_kwargs={"mirostat": 0},
)

# 设置嵌入模型
Settings.embed_model = ollama_embedding

# 读取本地数据
documents = SimpleDirectoryReader("./data").load_data()

# 设置大语言模型
Settings.llm = Ollama(model="deepseek-r1:7b", request_timeout=360.0, base_url="http://localhost:6006")

# 把本地数据向量化
index = VectorStoreIndex.from_documents(
    documents,
)
# 初始化搜索引擎
query_engine = index.as_query_engine()
# 开始搜索
response = query_engine.query("张辉是谁?")
print(response)

