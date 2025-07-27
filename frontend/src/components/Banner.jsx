import React from 'react';
import carousel1 from '../assets/eshopper/img/carousel-1.jpg';

const Banner = ({ headline, subtitle }) => {
  return (
    <div className="container-fluid mb-3">
      <div className="relative h-96 overflow-hidden rounded-lg shadow-lg">
        <img src={carousel1} alt="Banner" className="w-full h-full object-cover" />
        <div className="absolute inset-0 bg-black bg-opacity-50 flex flex-col items-center justify-center text-center p-4">
          <h4 className="text-white text-lg md:text-xl lg:text-2xl font-medium mb-2">
            {subtitle}
          </h4>
          <h3 className="text-white text-3xl md:text-4xl lg:text-5xl font-semibold mb-4">
            {headline}
          </h3>
          <a href="#" className="px-6 py-3 bg-white text-gray-800 font-semibold rounded-lg shadow-md hover:bg-gray-100 transition duration-300">
            Shop Now
          </a>
        </div>
      </div>
    </div>
  );
};

export default Banner;


