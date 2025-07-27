import PropTypes from 'prop-types'

function ProductCard({ imageUrl, title, price, oldPrice }) {
  return (
    <div className="border rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300 flex flex-col bg-white dark:bg-gray-800">
      <div className="overflow-hidden">
        <img
          src={imageUrl}
          alt={title}
          className="w-full h-48 md:h-60 object-cover"
        />
      </div>
      <div className="flex-1 p-4 text-center">
        <h3 className="text-sm font-medium text-gray-700 dark:text-gray-100 truncate mb-2">
          {title}
        </h3>
        <div className="flex justify-center gap-2 text-gray-900 dark:text-white">
          {oldPrice && (
            <span className="line-through text-gray-400 text-sm">{oldPrice}</span>
          )}
          <span className="font-semibold">{price}</span>
        </div>
      </div>
      <div className="flex justify-between items-center bg-gray-100 dark:bg-gray-700 px-4 py-2 text-sm">
        <button className="text-blue-600 hover:underline">View Detail</button>
        <button className="text-blue-600 hover:underline">Add To Cart</button>
      </div>
    </div>
  )
}

ProductCard.propTypes = {
  imageUrl: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  price: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
  oldPrice: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
}

ProductCard.defaultProps = {
  oldPrice: null,
}

export default ProductCard
