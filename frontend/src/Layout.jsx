import React from 'react'

// Components will be implemented and exported later
import Header from './Header'
import Footer from './Footer'

/**
 * Page wrapper for the eShopper theme
 */
export default function Layout({ children }) {
  return (
    <div className="flex min-h-screen flex-col bg-gray-50">
      {/* Header placeholder */}
      <Header />
      {/* Main content */}
      <main className="container mx-auto flex-1 p-4">{children}</main>
      {/* Footer placeholder */}
      <Footer />
    </div>
  )
}
