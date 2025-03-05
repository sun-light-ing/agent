from ownembedding import OwnEmbeddings
from ownllm import RemoteAPILLM
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
import os

os.environ['OPENAI_API_KEY'] = 'sk-tfdnbyicwpwykcekltgfwyljnwyevgscsgcvtsylxiyrxiow'

# 读取本地数据
documents = SimpleDirectoryReader("./data").load_data()

# 将 documents 转换为字符串
input_content = " ".join([doc.text for doc in documents])

embedding = OwnEmbeddings(
    model_url="https://api.siliconflow.cn/v1/embeddings",
    model_name="BAAI/bge-large-zh-v1.5",
    model_apikey="sk-tfdnbyicwpwykcekltgfwyljnwyevgscsgcvtsylxiyrxiow",
    input_content=input_content  # 传入字符串
)

llm = RemoteAPILLM(
    api_url="https://api.siliconflow.cn/v1/chat/completions",
    api_key="sk-tfdnbyicwpwykcekltgfwyljnwyevgscsgcvtsylxiyrxiow",
    model_name="deepseek-ai/DeepSeek-R1"
)

Settings.embed_model = embedding
Settings.llm = llm

# 把本地数据向量化
index = VectorStoreIndex.from_documents(
    documents,
)
# 初始化搜索引擎
query_engine = index.as_query_engine()
# 开始搜索
response = query_engine.query("宋俊伟是谁?")
print(response)
