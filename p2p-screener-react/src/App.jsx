import { useState } from 'react'
import './App.css'
import { AppLayout } from './AppLayout'
import { MainContainer } from './MainContainer'
import { ConfigProvider } from 'antd'

function App() {

  return (
    <ConfigProvider
      theme={{
        components: {
          Layout: {
            // bodyBg: '7DC6EF',
            // footerBg: '7DC6EF'
          }
        }
      }}
    >
      <div style={{ paddingLeft: '10rem', paddingRight: '10rem' }}>
        <AppLayout />
      </div>

    </ConfigProvider>


  )
}

export default App
