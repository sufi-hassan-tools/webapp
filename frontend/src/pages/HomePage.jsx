import React from 'react';
import Layout from '../components/Layout';
import ProductCard from '../components/ProductCard';
import product1 from '../assets/eshopper/img/product-1.jpg';
import product2 from '../assets/eshopper/img/product-2.jpg';
import product3 from '../assets/eshopper/img/product-3.jpg';
import product4 from '../assets/eshopper/img/product-4.jpg';
import product5 from '../assets/eshopper/img/product-5.jpg';
import product6 from '../assets/eshopper/img/product-6.jpg';
import product7 from '../assets/eshopper/img/product-7.jpg';
import product8 from '../assets/eshopper/img/product-8.jpg';
import cat1 from '../assets/eshopper/img/cat-1.jpg';
import cat2 from '../assets/eshopper/img/cat-2.jpg';
import cat3 from '../assets/eshopper/img/cat-3.jpg';

const HomePage = () => {
  const dummyProducts = [
    {
      imageUrl: product1,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product2,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product3,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product4,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product5,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product6,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product7,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
    {
      imageUrl: product8,
      title: 'Colorful Stylish Shirt',
      price: 123.00,
      oldPrice: 150.00,
    },
  ];

  return (
    <Layout>
      {/* Features/Services Section */}
      <div className="container-fluid pt-5">
        <div className="row px-xl-5 pb-3">
          <div className="col-lg-3 col-md-6 col-sm-12 pb-1">
            <div className="d-flex align-items-center border mb-4" style={{ padding: '30px' }}>
              <h1 className="fa fa-check text-primary m-0 mr-3"></h1>
              <h5 className="font-weight-semi-bold m-0">Quality Product</h5>
            </div>
          </div>
          <div className="col-lg-3 col-md-6 col-sm-12 pb-1">
            <div className="d-flex align-items-center border mb-4" style={{ padding: '30px' }}>
              <h1 className="fa fa-shipping-fast text-primary m-0 mr-2"></h1>
              <h5 className="font-weight-semi-bold m-0">Free Shipping</h5>
            </div>
          </div>
          <div className="col-lg-3 col-md-6 col-sm-12 pb-1">
            <div className="d-flex align-items-center border mb-4" style={{ padding: '30px' }}>
              <h1 className="fas fa-exchange-alt text-primary m-0 mr-3"></h1>
              <h5 className="font-weight-semi-bold m-0">14-Day Return</h5>
            </div>
          </div>
          <div className="col-lg-3 col-md-6 col-sm-12 pb-1">
            <div className="d-flex align-items-center border mb-4" style={{ padding: '30px' }}>
              <h1 className="fa fa-phone-volume text-primary m-0 mr-3"></h1>
              <h5 className="font-weight-semi-bold m-0">24/7 Support</h5>
            </div>
          </div>
        </div>
      </div>

      {/* Categories Section */}
      <div className="container-fluid pt-5">
        <div className="row px-xl-5 pb-3">
          <div className="col-lg-4 col-md-6 pb-1">
            <div className="cat-item d-flex flex-column border mb-4" style={{ padding: '30px' }}>
              <p className="text-right">15 Products</p>
              <a href="" className="cat-img position-relative overflow-hidden mb-3">
                <img className="img-fluid" src={cat1} alt="" />
              </a>
              <h5 className="font-weight-semi-bold m-0">Electronics</h5>
            </div>
          </div>
          <div className="col-lg-4 col-md-6 pb-1">
            <div className="cat-item d-flex flex-column border mb-4" style={{ padding: '30px' }}>
              <p className="text-right">15 Products</p>
              <a href="" className="cat-img position-relative overflow-hidden mb-3">
                <img className="img-fluid" src={cat2} alt="" />
              </a>
              <h5 className="font-weight-semi-bold m-0">Fashion</h5>
            </div>
          </div>
          <div className="col-lg-4 col-md-6 pb-1">
            <div className="cat-item d-flex flex-column border mb-4" style={{ padding: '30px' }}>
              <p className="text-right">15 Products</p>
              <a href="" className="cat-img position-relative overflow-hidden mb-3">
                <img className="img-fluid" src={cat3} alt="" />
              </a>
              <h5 className="font-weight-semi-bold m-0">Home Goods</h5>
            </div>
          </div>
        </div>
      </div>

      {/* Products Section */}
      <div className="container-fluid pt-5">
        <div className="text-center mb-4">
          <h2 className="section-title px-5"><span className="px-2">Our Products</span></h2>
        </div>
        <div className="row px-xl-5 pb-3">
          {dummyProducts.map((product, index) => (
            <ProductCard
              key={index}
              imageUrl={product.imageUrl}
              title={product.title}
              price={product.price}
              oldPrice={product.oldPrice}
            />
          ))}
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;

