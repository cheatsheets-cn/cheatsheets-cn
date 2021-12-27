>cstable
>| bin/kafka-topics.sh --create \
    --bootstrap-server 127.0.0.1:9092 \
    --replication-factor 1 --partitions 1 --topic test || 创建 topic test |<
>| bin/kafka-topics.sh --list \
    --bootstrap-server 127.0.0.1:9092 || 列出已创建的 topic |<
>| bin/kafka-console-producer.sh \
    --bootstrap-server 127.0.0.1:9092 \
    --topic test || 向 topic 发送信息 |<
>| bin/kafka-console-consumer.sh \
    --bootstrap-server 127.0.0.1:9092 \
    --topic test --from-beginning || 启动消费者接收 topic 消息 |<
<cstable