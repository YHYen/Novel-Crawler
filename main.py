import tensorflow as tf
import tensorflow_hub as hub

# 加载模型
elmo = hub.load("https://tfhub.dev/google/elmo/2")
# 输入的数据集
embeddings = elmo.signatures["default"](tf.constant([
                "i like green eggs and ham",
                "i like green ham and eggs"
                ])
                )["elmo"]

print(embeddings)