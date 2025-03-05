from pydantic import Field
from llama_index.core.base.llms.types import LLMMetadata
from llama_index.core.llms import CustomLLM, CompletionResponse
import requests

class RemoteAPILLM(CustomLLM):
    api_url: str = Field(description="The URL of the embedding model API.")
    model_name: str = Field(description="The name of the embedding model.")
    api_key: str = Field(description="The API key for the embedding model.")

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            model_name=self.model_name,
            context_window=4096,  # Adjust based on your model's context window
            num_output=512,  # Adjust based on your model's output length
            is_chat_model=True,  # Set to False if it's not a chat model
        )

    def __init__(self, api_url: str, api_key: str, model_name: str):
        super().__init__(api_url=api_url, api_key=api_key, model_name=model_name)

    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        """调用远程 API 完成文本生成"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            **kwargs  # 其他参数
        }
        response = requests.post(self.api_url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return CompletionResponse(text=result["choices"][0]['message']['content'])
        else:
            raise ValueError(f"API request failed: {response.status_code} {response.text}")

    def stream_complete(self, prompt: str, **kwargs):
        """流式生成文本（如果需要）"""
        raise NotImplementedError("Streaming not supported for this LLM.")


# remote_llm = RemoteAPILLM(
#     api_url="https://api.siliconflow.cn/v1/chat/completions",
#     api_key="sk-tfdnbyicwpwykcekltgfwyljnwyevgscsgcvtsylxiyrxiow",
#     model_name="deepseek-ai/DeepSeek-R1"
# )
# prompt = '介绍一下你自己'
# response = remote_llm.complete(prompt)
# print(response.text)
