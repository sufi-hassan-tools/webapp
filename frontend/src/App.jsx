import './index.css'
import Header from './Header.jsx'

function App() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-900 text-gray-900 dark:text-white p-8">
      <Header />
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 rounded bg-gray-100 dark:bg-gray-800">Sales: 123</div>
        <div className="p-4 rounded bg-gray-100 dark:bg-gray-800">Orders: 45</div>
        <div className="p-4 rounded bg-gray-100 dark:bg-gray-800">Users: 78</div>
      </div>
    </div>
  )
}

export default App
