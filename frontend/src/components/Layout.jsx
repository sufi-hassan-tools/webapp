import React from 'react';

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="bg-gray-200 p-4">
        {/* Header component will be imported here */}
        <p>Header Placeholder</p>
      </header>
      <main className="flex-grow container mx-auto p-4">
        {children}
      </main>
      <footer className="bg-gray-800 text-white p-4">
        {/* Footer component will be imported here */}
        <p>Footer Placeholder</p>
      </footer>
    </div>
  );
};

export default Layout;


