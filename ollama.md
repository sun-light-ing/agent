#### 运行Ollama和Deepseek的GPU电脑选购标准：

1.至少4核CPU

2.至少8G运行内存

3.存储至少10G



英伟达的GTCX 1650 4GB(显卡)

AMD RX的4GB(显卡)，16GB内存





```bash
# 设置环境变量
sudo vi /etc/profile # 系统级别

vi ~/.bash_profile  # 用户级别


vi ~/.bashrc

export OLLAMA_HOST="0.0.0.0:6006"
export OLLAMA_MODELS=/root/autodl-tmp/models

source


# 下载ollama
curl -fsSL https://ollama.com/install.sh -o ollama_install.sh

# 修改源仓库，加速下载
sed -i 's|https://ollama.com/download/ollama-linux|https://gh.llkk.cc/https://github.com/ollama/ollama/releases/download/v0.5.7/ollama-linux|g' ollama_install.sh

# 赋予权限
chmod +x ollama_install.sh

# 下载ollama
sh ollama_install.sh

# 运行ollama服务
nohup ollama serve

# 拉取deepseek
ollama run deepseek-r1:7b

# 拉取嵌入模型
ollama pull bge-m3


ollama run bge-m3


# 开启学术加速
source /etc/network_turbo

# 取消学术加速
unset http_proxy && unset https_proxy


```









https://blog.csdn.net/weixin_43196262/article/details/138841082

https://zhuanlan.zhihu.com/p/836550833

https://www.cnblogs.com/qubernet/p/18702147

https://blog.csdn.net/willian113/article/details/142746017









