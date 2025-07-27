import React from 'react';

const Header = () => {
  return (
    <div className="container-fluid">
        <div className="row bg-secondary py-2 px-xl-5">
            <div className="col-lg-6 d-none d-lg-block">
                <div className="d-inline-flex align-items-center">
                    <a className="text-dark" href="#">FAQs</a>
                    <span className="text-muted px-2">|</span>
                    <a className="text-dark" href="#">Help</a>
                    <span className="text-muted px-2">|</span>
                    <a className="text-dark" href="#">Support</a>
                </div>
            </div>
            <div className="col-lg-6 text-center text-lg-right">
                <div className="d-inline-flex align-items-center">
                    <a className="text-dark px-2" href=""><i className="fab fa-facebook-f"></i></a>
                    <a className="text-dark px-2" href=""><i className="fab fa-twitter"></i></a>
                    <a className="text-dark px-2" href=""><i className="fab fa-linkedin-in"></i></a>
                    <a className="text-dark px-2" href=""><i className="fab fa-instagram"></i></a>
                    <a className="text-dark pl-2" href=""><i className="fab fa-youtube"></i></a>
                </div>
            </div>
        </div>
        <div className="row align-items-center py-3 px-xl-5">
            <div className="col-lg-3 d-none d-lg-block">
                <a href="/" className="text-decoration-none">
                    <h1 className="m-0 display-5 font-weight-semi-bold"><span className="text-primary font-weight-bold border px-3 mr-1">M</span>oohaar</h1>
                </a>
            </div>
            <div className="col-lg-6 col-6 text-left">
                <form action="">
                    <div className="input-group">
                        <input type="text" className="form-control" placeholder="Search for products"/>
                        <div className="input-group-append">
                            <span className="input-group-text bg-transparent text-primary"><i className="fa fa-search"></i></span>
                        </div>
                    </div>
                </form>
            </div>
            <div className="col-lg-3 col-6 text-right">
                <a href="" className="btn border"><i className="fas fa-heart text-primary"></i><span className="badge">0</span></a>
                <a href="" className="btn border"><i className="fas fa-shopping-cart text-primary"></i><span className="badge">0</span></a>
            </div>
        </div>
    </div>

    <div className="container-fluid">
        <div className="row border-top px-xl-5">
            <div className="col-lg-3 d-none d-lg-block">
                <a className="btn shadow-none d-flex align-items-center justify-content-between bg-primary text-white w-100" data-toggle="collapse" href="#navbar-vertical" style={{height: '65px', marginTop: '-1px', padding: '0 30px'}}>
                    <h6 className="m-0">Categories</h6>
                    <i className="fa fa-angle-down text-dark"></i>
                </a>
                <nav className="collapse position-absolute navbar navbar-vertical navbar-light align-items-start p-0 border border-top-0 border-bottom-0 bg-light" id="navbar-vertical" style={{width: 'calc(100% - 30px)', zIndex: 1}}>
                    <div className="navbar-nav w-100 overflow-hidden" style={{height: '410px'}}>
                        {/* This will be made dynamic later */}
                        <a href="" className="nav-item nav-link">Shirts</a>
                        <a href="" className="nav-item nav-link">Jeans</a>
                    </div>
                </nav>
            </div>
            <div className="col-lg-9">
                <nav className="navbar navbar-expand-lg bg-light navbar-light py-3 py-lg-0 px-0">
                    <a href="" className="text-decoration-none d-block d-lg-none">
                        <h1 className="m-0 display-5 font-weight-semi-bold"><span className="text-primary font-weight-bold border px-3 mr-1">M</span>oohaar</h1>
                    </a>
                    <button type="button" className="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse justify-content-between" id="navbarCollapse">
                        <div className="navbar-nav mr-auto py-0">
                            <a href="#" className="nav-item nav-link active">Home</a>
                            <a href="#" className="nav-item nav-link">Shop</a>
                            <a href="#" className="nav-item nav-link">Contact</a>
                        </div>
                        <div className="navbar-nav ml-auto py-0">
                            {/* Django template tags removed, will need React-based authentication */}
                            <a href="#" className="nav-item nav-link">Login</a>
                            <a href="#" className="nav-item nav-link">Register</a>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </div>
    </div >
  );
};

export default Header;


