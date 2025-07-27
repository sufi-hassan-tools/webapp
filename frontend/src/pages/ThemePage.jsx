import React from 'react';
import { useParams } from 'react-router-dom';
import Layout from '../components/Layout';

const ThemePage = () => {
  const { storeId } = useParams();

  return (
    <Layout>
      <div className="container mx-auto p-4">
        <h2 className="text-2xl font-bold mb-4">Welcome to ThemePage: {storeId}</h2>
        <p>This is a placeholder page for the theme.</p>
      </div>
    </Layout>
  );
};

export default ThemePage;


