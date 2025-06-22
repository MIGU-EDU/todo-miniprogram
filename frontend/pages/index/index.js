import { addTodo, updateStatus, delTodo, getTodo } from '../../api/todo.js'

Page({
  data: {
    value: '',
    disabled: true,
    todo: []
  },

  async onShow() {
    // 页面显示时获取待办事项，延时1秒确保登录完成
    setTimeout(() => {
      this.loadTodos()
    }, 1000)
  },

  // 加载待办事项的方法
  async loadTodos() {
    try{
      let result = await getTodo()
      this.setData({
        todo: result
      })
    } catch(err) {
      console.log('获取待办事项失败:', err)
    }
  },

  // 输入框内容变化时更新值
  onChange(e) {
    this.setData({
      value: e.detail,
      disabled: e.detail.length === 0
    });
  },

  // 添加新待办事项
  async add() {
    if (!this.data.value.trim()) return;
    
    const newTodo = {
      title: this.data.value
    };
    
    try {
      await addTodo(newTodo)
      // 添加成功后清空输入框并刷新列表
      this.setData({
        value: '',
        disabled: true
      });
      // 刷新待办事项列表
      this.loadTodos()
    } catch (err) {
      console.log('添加待办事项失败:', err)
    }
  },

  // 标记待办事项为已完成
  async completeTodo(e) {
    console.log(e)
    const index = e.currentTarget.dataset.index;
    const newTodoList = [...this.data.todo];
    
    // 修改指定下标的待办事项状态
    newTodoList[index].completed = true;
    
    // 更新数据，触发视图更新
    this.setData({
      todo: newTodoList
    });

    // 构造参数
    const params = {
      todo_id: newTodoList[index].id,
      completed: true
    }

    const res = await updateStatus(params)
    console.log(res)
  },

  // 删除待办事项
  async deleteTodo(e) {
    const index = e.currentTarget.dataset.index;
    const id = this.data.todo[index].id
    try {
      await delTodo({ todo_id: id})
      // 刷新待办事项列表
      this.loadTodos()
    } catch (err) {
      console.log('删除待办事项失败:', err)
    }
  }
});
