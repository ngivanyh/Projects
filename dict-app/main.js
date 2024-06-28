const { app, BrowserWindow } = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
      width: 325,
      height: 430,
      resizable: false
    })
  
    win.loadURL('http://127.0.0.1:5000')
}

app.whenReady().then(() => {
    createWindow()
})

// const PY_DIST_FOLDER = 'word-app'
// const PY_FOLDER = './'
// const PY_MODULE = 'app' // without .py suffix

// const guessPackaged = () => {
//   const fullPath = path.join(__dirname, PY_DIST_FOLDER)
//   return require('fs').existsSync(fullPath)
// }

// const getScriptPath = () => {
//   if (!guessPackaged()) {
//     return path.join(__dirname, PY_FOLDER, PY_MODULE + '.py')
//   }
//   if (process.platform === 'win32') {
//     return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE + '.exe')
//   }
//   return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE)
// }