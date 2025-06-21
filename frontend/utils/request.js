import { showToast } from './util'

function request(url, service, method, params, header) {
  let pullUrl = url + service
  header = header || {}

  let accessToken = wx.getStorageSync('token')
  if (accessToken) {
    header['Authorization'] = `Bearer ${accessToken}`
  }
  
  return new Promise((resolve, reject) => {
    wx.request({
      url: pullUrl,
      data: params || {},
      method: method || 'get',
      header: header,
      success: (res) => {
        if (res.statusCode == 200) {
          resolve(res.data)
        } else {
          wx.showToast({
            title: '服务器繁忙，请稍后再试',
            icon: 'none',
          })
          reject(res.data)
        }
      },
      fail: (err) => {
        reject(err)
      }
    })
  })
}

const wxRequest = {
  get: (url, service, params) => {
    return request(url, service, 'get', params, {
      'content-type': 'application/x-www-form-urlencoded',
    })
  },
  post: (url, service, params) => {
    return request(url, service, 'post', params, {
      'content-type': 'application/json'
    })
  },
  put: (url, service, params,contentType) => {
    return request(url, service, 'put', params, {
      'content-type': contentType ? contentType :'application/json'
    })
  },
  delete: (url, service, params) => {
    return request(url, service, 'delete', params, {
      'content-type': 'application/json'
    })
  }
}

export default wxRequest
