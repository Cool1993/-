# opsany接口操作脚本

## 基本功能
同步对应的数据到opsany平台
1. 比对资源平台、云管平台、管控平台、Prometheus的主机数量差异，输出结果保存到output目录下
2. 同步所有云平台对外开放的公网ip，保存到资源平台-资源仓库-其它-云平台公网ip
3. 同步所有云平台的中间件、数据库的利用率数据，保存到资源平台-资源仓库-其它-中间件低利用率
## 使用方式
### 安装依赖
pip install -r requirements.txt # 安装依赖
### 参考example修改配置
- src/config/config.py
- src/config/keys_ali.yaml
- src/config/keys_aws.yaml
### 运行
python main.py