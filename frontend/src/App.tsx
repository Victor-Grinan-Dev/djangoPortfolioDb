// import { useState } from 'react'
import Home from './pages/Home'
import { Route, createBrowserRouter,
  RouterProvider,
  createRoutesFromElements,} from "react-router-dom"


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path='/' element={<Home/>} />
    </Route>
  )
);

const App: React.FC = () => {
    return <RouterProvider router={router} />;
  }


export default App
