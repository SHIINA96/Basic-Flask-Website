from app import app

if __name__ == '__main__':
    # 在使用debug模式后，Flask可以实时更新新的变化 
    # 定义host与port，指定访问页面的地址
     app.run(debug=True, host='127.0.0.1', port=3000)