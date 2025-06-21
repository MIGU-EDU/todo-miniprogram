export const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return `${[year, month, day].map(formatNumber).join('/')} ${[hour, minute, second].map(formatNumber).join(':')}`
}

export const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : `0${n}`
}

/**
 * 显示toast
 */
export const showToast = (title = '操作成功', icon = 'none') => {
  // 为了wx.showToast能够在try.finish(hideLoading)之后执行，加一个10毫秒的定时器，解决真机模式下hideLoading隐藏wx.showToast的弹窗问题
  setTimeout(() => {
    wx.showToast({
      title,
      icon,
      duration: 2000
    })
  }, 100)
}