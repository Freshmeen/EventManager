import { useAction, useAtom } from '@reatom/npm-react'
import { useEffect } from 'react'
import './App.css'
import { callPopup, userTypeAtom } from './model/actions'
import { BasePopup } from './popups/BasePopup/basePopup'
import { MainPage } from './views/MainPage/mainPage'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'

function App() {
  const [userType] = useAtom(userTypeAtom)
  const callLoginPopup = useAction(callPopup)

  useEffect(() => {
    if (userType == null) {
      callLoginPopup("login")
    }
  }, [userType, callLoginPopup])

  return (
    <BrowserRouter>
      <Routes>
        <Route 
          path="/" 
          element={<Navigate to={userType ? "/main" : "/login"} replace />} 
        />
        <Route path="/login" element={<BasePopup />} />
        <Route path="/main" element={<MainPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App