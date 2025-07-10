const env = "prod";
let config = {};

if (env === "dev") {
  // 开发环境
  config = {
    apiBaseUrl:'http://localhost:8003',
  }
} else {
  // 生产环境
  config = {
    apiBaseUrl:'https://www.todo.miguyouke.com',
  }
}

export { config, env };
