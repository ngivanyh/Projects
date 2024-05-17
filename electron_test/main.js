const { app, BrowserWindow } = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
      width: 325,
      height: 430,
      resizable: false
    })
  
    win.loadFile('index.html')
}

app.whenReady().then(() => {
    createWindow()
})