# SaveFlow Todo API

一个使用 FastAPI + SQLModel + PostgreSQL 构建的待办事项 API 应用，参考了 [FastAPI 官方全栈模板](https://github.com/fastapi/full-stack-fastapi-template) 的最佳实践。

## 🚀 功能特性

- ⚡ **FastAPI** - 现代、快速的 Web 框架
- 🧰 **SQLModel** - FastAPI 作者开发的 ORM，完美集成 FastAPI 和 Pydantic
- 💾 **PostgreSQL** - 强大的关系型数据库
- 🔄 **Alembic** - 轻量级数据库迁移工具
- 🐳 **Docker** - 容器化部署
- 📚 **自动 API 文档** - Swagger UI 和 ReDoc
- 🔧 **类型提示** - 完整的 Python 类型支持
- 🎯 **CRUD 操作** - 完整的增删改查功能

## 📁 项目结构

```
saveflow-backend/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── todos.py        # 待办事项路由
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py           # 应用配置
│   │   └── database.py         # 数据库配置
│   ├── models/
│   │   └── todo.py             # 数据模型
│   ├── alembic/                # Alembic 迁移脚本
│   │   └── versions/
│   ├── __init__.py
│   └── main.py                 # FastAPI 应用
├── alembic.ini                 # Alembic 配置文件
├── docker-compose.yml          # Docker 开发环境配置
├── Dockerfile                  # 应用 Dockerfile
├── pyproject.toml              # 项目配置和依赖
├── .env                        # 环境变量（需要创建）
└── README.md
```

## 🔧 安装和设置

### 1. 克隆项目

```bash
git clone <repository-url>
cd saveflow-backend
```

### 2. 环境配置

创建 `.env` 文件，复制 `.env.example` (如果存在) 或使用以下内容：

```env
# 数据库配置
# 如果使用 docker-compose 启动，请使用下面的配置
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/saveflow

# 如果在本地直接运行应用 (不通过 docker)
# DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/saveflow

# 应用配置
DEBUG=True
```

### 3. 启动应用 (使用 Docker)

这是推荐的启动方式，可以一键启动应用和数据库。

```bash
docker compose up -d
```

应用将在 `http://localhost:8003` 启动。

### 4. 数据库迁移 (Alembic)

当你修改了 `app/models/` 中的数据模型后，你需要创建新的迁移脚本并应用它。

**1. 创建迁移脚本** (在 backend 容器内执行)

```bash
# 进入 backend 容器
docker compose exec backend bash

# 创建迁移脚本 (在容器内)
alembic revision --autogenerate -m "Some description of the change"

# 退出容器
exit
```

**2. 应用数据库迁移**

当有新的迁移脚本时，`docker compose up` 会自动应用迁移。如果需要手动应用：

```bash
docker compose up -d db # 启动数据库
fastapi dev app/main.py --port 8003 # 启动应用
```

## 📚 API 文档

启动应用后，访问以下地址查看 API 文档：

- **Swagger UI**: http://localhost:8003/docs
- **ReDoc**: http://localhost:8003/redoc

## 🔗 API 端点

### 基础端点
- `GET /` - 应用信息
- `GET /health` - 健康检查

### 待办事项 API
- `POST /api/v1/todos/` - 创建待办事项
- `GET /api/v1/todos/` - 获取待办事项列表（支持分页和筛选）
- `GET /api/v1/todos/{id}` - 获取单个待办事项
- `PUT /api/v1/todos/{id}` - 更新待办事项
- `DELETE /api/v1/todos/{id}` - 删除待办事项

## 📝 数据模型

### 待办事项模型

```json
{
  "id": 1,
  "title": "学习 FastAPI",
  "description": "完成 FastAPI 教程和项目实践",
  "completed": false,
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": null
}
```

## 🧪 测试示例 (使用 cURL)

### 创建待办事项
```bash
curl -X POST "http://localhost:8003/api/v1/todos/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "学习 SQLModel",
       "description": "掌握 SQLModel 的基本用法",
       "completed": false
     }'
```

### 获取待办事项列表
```bash
curl "http://localhost:8003/api/v1/todos/"
```

## 🛠️ 技术栈

- **FastAPI**: 现代 Python Web 框架
- **SQLModel**: 类型安全的 ORM，集成 SQLAlchemy 和 Pydantic
- **PostgreSQL**: 关系型数据库
- **Alembic**: 数据库迁移
- **Docker & Docker Compose**: 容器化
- **Uvicorn**: ASGI 服务器
- **UV**: Python 包管理器

## 📖 参考资料

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLModel 官方文档](https://sqlmodel.tiangolo.com/)
- [Alembic 官方文档](https://alembic.sqlalchemy.org/)
- [FastAPI 官方全栈模板](https://github.com/fastapi/full-stack-fastapi-template)
