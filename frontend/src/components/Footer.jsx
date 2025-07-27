import React from 'react';

const Footer = () => {
  return (
    <footer className="container-fluid bg-secondary text-dark mt-5 pt-5">
        <div className="row px-xl-5 pt-5">
            <div className="col-lg-4 col-md-12 mb-5 pr-3 pr-xl-5">
                <a href="" className="text-decoration-none">
                    <h1 className="mb-4 display-5 font-weight-semi-bold"><span className="text-primary font-weight-bold border border-white px-3 mr-1">M</span>oohaar</h1>
                </a>
                <p>Brief description about the store here. Dolore erat dolor sit lorem vero amet.</p>
                <p className="mb-2"><i className="fa fa-map-marker-alt text-primary mr-3"></i>123 Street, Karachi, Pakistan</p>
                <p className="mb-2"><i className="fa fa-envelope text-primary mr-3"></i>info@moohaar.com</p>
                <p className="mb-0"><i className="fa fa-phone-alt text-primary mr-3"></i>+92 300 1234567</p>
            </div>
            <div className="col-lg-8 col-md-12">
                <div className="row">
                    <div className="col-md-4 mb-5">
                        <h5 className="font-weight-bold text-dark mb-4">Quick Links</h5>
                        <div className="d-flex flex-column justify-content-start">
                            <a className="text-dark mb-2" href="#"><i className="fa fa-angle-right mr-2"></i>Home</a>
                            <a className="text-dark mb-2" href="#"><i className="fa fa-angle-right mr-2"></i>Our Shop</a>
                            <a className="text-dark" href="#"><i className="fa fa-angle-right mr-2"></i>Contact Us</a>
                        </div>
                    </div>
                    <div className="col-md-4 mb-5">
                        <h5 className="font-weight-bold text-dark mb-4">Customer Service</h5>
                        <div className="d-flex flex-column justify-content-start">
                             <a className="text-dark mb-2" href="#"><i className="fa fa-angle-right mr-2"></i>FAQs</a>
                             <a className="text-dark mb-2" href="#"><i className="fa fa-angle-right mr-2"></i>Returns</a>
                             <a className="text-dark mb-2" href="#"><i className="fa fa-angle-right mr-2"></i>Shipping</a>
                        </div>
                    </div>
                    <div className="col-md-4 mb-5">
                        <h5 className="font-weight-bold text-dark mb-4">Newsletter</h5>
                        <form action="">
                            <div className="form-group">
                                <input type="text" className="form-control border-0 py-4" placeholder="Your Name" required="required" />
                            </div>
                            <div className="form-group">
                                <input type="email" className="form-control border-0 py-4" placeholder="Your Email" required="required" />
                            </div>
                            <div><button className="btn btn-primary btn-block border-0 py-3" type="submit">Subscribe Now</button></div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div className="row border-top border-light mx-xl-5 py-4">
            <div className="col-md-6 px-xl-0">
                <p className="mb-md-0 text-center text-md-left text-dark">
                    &copy; <a className="text-dark font-weight-semi-bold" href="#">Your Store</a>. All Rights Reserved.
                </p>
            </div>
            <div className="col-md-6 px-xl-0 text-center text-md-right">
                 <p className="mb-md-0 text-center text-md-right text-dark">
                    Powered by <a className="text-dark font-weight-semi-bold" href="#">Moohaar</a>
                </p>
            </div>
        </div>
    </footer>
  );
};

export default Footer;


