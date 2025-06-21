import wxRequest from '../utils/request'
import { config } from '../config/index'

export const login = (params) => {
  return wxRequest.post(
    config.apiBaseUrl,
    '/api/v1/auth/wechat/login',
    params
  )
}
