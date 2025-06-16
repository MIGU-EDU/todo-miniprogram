from datetime import datetime
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlmodel import select

from app.core.auth import create_access_token, CurrentUser
from app.core.database import AsyncSessionDep
from app.models.user import User, UserCreate
from app.services.wechat import WeChatService

router = APIRouter(prefix="/auth", tags=["认证"])


class WeChatLoginRequest(BaseModel):
    """微信登录请求模型"""
    code: str
    nickname: str = ""
    avatar_url: str = ""


class LoginResponse(BaseModel):
    """登录响应模型"""
    access_token: str
    token_type: str = "bearer"
    user_id: int
    openid: str


@router.post("/wechat/login", response_model=LoginResponse)
async def wechat_login(
    login_data: WeChatLoginRequest,
    session: AsyncSessionDep
) -> LoginResponse:
    """微信小程序登录"""
    
    # 通过code换取openid
    wechat_data = await WeChatService.code_to_session(login_data.code)
    openid = wechat_data.get("openid")
    
    if not openid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="获取openid失败"
        )
    
    # 查找或创建用户
    statement = select(User).where(User.openid == openid)
    result = await session.exec(statement)
    user = result.first()
    
    if not user:
        # 创建新用户
        user_data = UserCreate(
            openid=openid,
            nickname=login_data.nickname,
            avatar_url=login_data.avatar_url
        )
        user = User.model_validate(user_data)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    else:
        # 更新用户信息
        if login_data.nickname:
            user.nickname = login_data.nickname
        if login_data.avatar_url:
            user.avatar_url = login_data.avatar_url
        user.updated_at = datetime.utcnow()
        session.add(user)
        await session.commit()
        await session.refresh(user)
    
    # 生成JWT token
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return LoginResponse(
        access_token=access_token,
        user_id=user.id,
        openid=user.openid
    )


@router.get("/me")
async def get_current_user_info(current_user: CurrentUser):
    """获取当前用户信息"""
    return {
        "id": current_user.id,
        "openid": current_user.openid,
        "nickname": current_user.nickname,
        "avatar_url": current_user.avatar_url,
        "created_at": current_user.created_at
    } 