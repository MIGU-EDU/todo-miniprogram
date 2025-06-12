# SaveFlow Todo API

一个使用 FastAPI + SQLModel + PostgreSQL 构建的待办事项 API 应用，参考了 [FastAPI 官方全栈模板](https://github.com/fastapi/full-stack-fastapi-template) 的最佳实践。

## 🚀 功能特性

- ⚡ **FastAPI** - 现代、快速的 Web 框架
- 🧰 **SQLModel** - FastAPI 作者开发的 ORM，完美集成 FastAPI 和 Pydantic
- 💾 **PostgreSQL** - 强大的关系型数据库
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
│   │   │   └── todos.py          # 待办事项路由
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py             # 应用配置
│   │   └── database.py           # 数据库配置
│   ├── models/
│   │   └── todo.py               # 数据模型
│   ├── __init__.py
│   └── main.py                   # FastAPI 应用
├── pyproject.toml               # 项目配置和依赖
├── .env                         # 环境变量（需要创建）
└── README.md
```

## 🔧 安装和设置

### 1. 安装依赖

使用 UV 包管理器（推荐）：
```bash
uv sync
```

### 2. 环境配置

创建 `.env` 文件，配置你的数据库连接：
```env
# 数据库配置
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/saveflow_todos

# 应用配置
DEBUG=True
```

### 3. 数据库设置

确保 PostgreSQL 服务运行，并创建数据库：
```sql
CREATE DATABASE saveflow_todos;
```

### 4. 启动应用

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

## 🧪 测试示例

### 创建待办事项
```bash
curl -X POST "http://localhost:8000/api/v1/todos/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "学习 SQLModel",
       "description": "掌握 SQLModel 的基本用法",
       "completed": false
     }'
```

### 获取待办事项列表
```bash
curl "http://localhost:8000/api/v1/todos/"
```

## 🛠️ 技术栈

- **FastAPI**: 现代 Python Web 框架
- **SQLModel**: 类型安全的 ORM，集成 SQLAlchemy 和 Pydantic
- **PostgreSQL**: 关系型数据库
- **Uvicorn**: ASGI 服务器

## 📖 参考资料

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLModel 官方文档](https://sqlmodel.tiangolo.com/)
- [FastAPI 官方全栈模板](https://github.com/fastapi/full-stack-fastapi-template)
