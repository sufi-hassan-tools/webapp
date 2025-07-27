import Header from './Header';
import Footer from './Footer';
import Banner from './Banner';

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <Banner image="/src/assets/eshopper/img/carousel-1.jpg" headline="Quality Products" subtitle="10% Off Your First Order" />
      <main className="flex-grow container mx-auto p-4">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;


