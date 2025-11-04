import { reatomContext } from '@reatom/npm-react'
import App from './App'
import ReactDOM from 'react-dom/client'
import React from 'react'
import {createCtx} from "@reatom/core";


const ctx = createCtx();

ReactDOM.createRoot(document.getElementById('root')!).render(
    <reatomContext.Provider value={ctx}>
        <App />
    </reatomContext.Provider>
)
