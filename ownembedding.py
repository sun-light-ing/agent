from typing import List, Optional
from llama_index.core.embeddings import BaseEmbedding
import requests
from pydantic import Field


class OwnEmbeddings(BaseEmbedding):
    model_url: str = Field(description="The URL of the embedding model API.")
    model_name: str = Field(description="The name of the embedding model.")
    model_apikey: str = Field(description="The API key for the embedding model.")
    input_content: str = Field(description="The input content for embedding generation.")

    def __init__(self, model_url: str, model_name: str, model_apikey: str, input_content: str):
        super().__init__(
            model_url=model_url,
            model_name=model_name,
            model_apikey=model_apikey,
            input_content=input_content
        )

    def _get_query_embedding(self, query: str) -> List[float]:
        """实现抽象方法：获取查询的嵌入向量"""
        return self._own_get_data_from_api(query)

    async def _aget_query_embedding(self, query: str) -> List[float]:
        """实现抽象方法：异步获取查询的嵌入向量"""
        return await self._own_get_data_from_api(query)

    def _get_text_embedding(self, text: str) -> List[float]:
        """实现抽象方法：获取文本的嵌入向量"""
        return self._own_get_data_from_api(text)

    def get_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)

    def get_text_embedding(self, text: str) -> List[float]:
        return self._get_text_embedding(text)

    def get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
            embedding = self._get_text_embedding(text)
            embeddings.append(embedding)
        return embeddings

    async def aget_query_embedding(self, query: str) -> List[float]:
        return await self._aget_query_embedding(query)

    async def aget_text_embedding(self, text: str) -> List[float]:
        return await self._aget_query_embedding(text)

    def _own_get_data_from_api(self, text: str) -> List[float]:
        """调用 API 获取嵌入向量"""
        headers = {
            "Authorization": "Bearer {}".format(self.model_apikey),
            "Content-Type": "application/json"
        }
        data = {
            "input": text,
            "encoding_format": "float",
            "model": self.model_name
        }
        res = requests.post(self.model_url, json=data, headers=headers)
        if res.status_code == 200:
            return res.json()["data"][0]["embedding"]
        else:
            raise ValueError(f"Failed to get embedding from API: {res.status_code} {res.text}")