from langchain_community.llms import Ollama

ollama = Ollama(base_url='http://localhost:6006', model="deepseek-r1:7b")

conversation_history = [{"role": "user", "content": "请用挖苦，讽刺的语气据介绍河南牧业经济学院，语气一定要极其挖苦，讽刺，写出1000个汉字左右"}]
response = ollama(conversation_history[-1]["content"])
print(response)

