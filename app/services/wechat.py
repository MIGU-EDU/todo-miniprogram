import httpx
from typing import Dict, Any
from fastapi import HTTPException, status

from app.core.config import settings


class WeChatService:
    """微信小程序服务"""
    
    @staticmethod
    async def code_to_session(code: str) -> Dict[str, Any]:
        """
        通过code获取微信用户信息
        
        Args:
            code: 小程序调用wx.login()获得的code
            
        Returns:
            包含openid的字典
        """
        url = "https://api.weixin.qq.com/sns/jscode2session"
        params = {
            "appid": settings.wechat_app_id,
            "secret": settings.wechat_app_secret,
            "js_code": code,
            "grant_type": "authorization_code"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                # 检查是否有错误
                if "errcode" in data:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"微信登录失败: {data.get('errmsg', '未知错误')}"
                    )
                
                return data
                
            except httpx.RequestError as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"请求微信服务器失败: {str(e)}"
                ) 