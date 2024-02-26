import { useState } from 'react'
import Home from './pages/Home'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Home></Home>
      <h1 onClick={()=>setCount(count+1)}>Hello {count}</h1>
    </>
  )
}

export default App
