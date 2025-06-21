# 待办事项小程序

一个基于微信小程序和 Python 后端的待办事项管理应用。

## 项目概述

本项目是一个全栈的待办事项管理系统，包含：
- **微信小程序前端**：提供用户友好的移动端界面
- **Python 后端 API**：基于 FastAPI 框架，提供数据存储和用户认证功能

## 项目结构

```
todo-miniprogram/
├── backend/           # 后端 API 服务
│   ├── app/          # 应用核心代码
│   │   ├── api/      # API 路由
│   │   ├── core/     # 核心配置和认证
│   │   ├── models/   # 数据模型
│   │   └── services/ # 业务服务
│   ├── alembic/      # 数据库迁移
│   └── ...
├── frontend/         # 微信小程序前端
│   ├── pages/        # 小程序页面
│   ├── api/          # API 接口封装
│   ├── utils/        # 工具函数
│   └── ...
└── README.md
```

## 主要功能

- ✅ 用户注册和登录（微信授权）
- ✅ 创建、编辑、删除待办事项
- ✅ 待办事项状态管理
- ✅ 响应式小程序界面

## 技术栈

### 后端
- **Python 3.x**
- **FastAPI** - 现代化的 Web 框架
- **SQLAlchemy** - ORM 数据库操作
- **Alembic** - 数据库迁移管理
- **Docker** - 容器化部署

### 前端
- **微信小程序** - 原生小程序开发
- **JavaScript** - 业务逻辑实现

## 后端启动

查看 [backend/README.md](./backend/README.md).

## 前端启动

查看 [frontend/README.md](./frontend/README.md).

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。
