import wxRequest from '../utils/request'
import { config } from '../config/index'

export const addTodo = (params) => {
  return wxRequest.post(
    config.apiBaseUrl,
    '/api/v1/todos/',
    params
  )
}

export const updateStatus = (params) => {
  return wxRequest.put(
    config.apiBaseUrl,
    `/api/v1/todos/${params.todo_id}`,
    params
  )
}

export const delTodo = (params) => {
  return wxRequest.delete(
    config.apiBaseUrl,
    '/api/v1/todos/',
    params
  )
}

export const getTodo = () => {
  return wxRequest.get(
    config.apiBaseUrl,
    '/api/v1/todos/'
  )
}
