import Header from './Header';

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
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


