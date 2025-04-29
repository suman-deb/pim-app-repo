import logo from './logo.svg';
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:7071/api/products/') // Adjust the URL as Azure Function URL
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }
  , []); 



  return (
    <div className="App">
      <h1>🛒 Product Catalog</h1>
      {products.map(product => (
        <div key={product.productId} className="product-card">
          <h2>{product.name}</h2>
          <p>{product.description}</p>
          <strong>Price: ${product.price}</strong>
        </div>
      ))}
    </div>
  );
}

export default App;
