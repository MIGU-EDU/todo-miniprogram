// app.js
import { login } from './api/user.js'

App({
  onLaunch() {
    this.doLogin()
  },

  // 执行登录的方法
  async doLogin() {
    try {
      // 检查是否已有有效token
      const existingToken = wx.getStorageSync('token')
      if (existingToken) {
        console.log('已存在token，跳过登录')
        return
      }

      // 微信登录
      const loginResult = await this.wxLogin()
      const data = await login({ code: loginResult.code })
      
      wx.setStorageSync('token', data.access_token)
      console.log('登录成功')
    } catch (error) {
      console.error('登录失败:', error)
      // 登录失败后，可以选择重试或显示错误提示
      setTimeout(() => {
        this.doLogin()
      }, 3000)
    }
  },

  // 封装微信登录为Promise
  wxLogin() {
    return new Promise((resolve, reject) => {
      wx.login({
        success: (res) => {
          if (res.code) {
            resolve(res)
          } else {
            reject(new Error('获取微信登录code失败'))
          }
        },
        fail: (err) => {
          reject(err)
        }
      })
    })
  }
})
