const productService = require('../../src/services/product-service'); // Adjust the path as needed

describe('ProductService', () => {
  // Testing getAllProducts method
  describe('getAllProducts', () => {
    it('should return all products when no filters are applied', () => {
      const result = productService.getAllProducts();
      expect(result.products.length).toBeGreaterThan(0);
      expect(result).toHaveProperty('total');
      expect(result).toHaveProperty('limit');
      expect(result).toHaveProperty('offset');
    });

    it('should filter products by min price', () => {
      const result = productService.getAllProducts({ minPrice: 300 });
      expect(result.products.length).toBe(1);  // Adjusted to 1 product matching the min price filter
      expect(result.products.every(p => p.price >= 300)).toBe(true);
    });

    it('should filter products by max price', () => {
      const result = productService.getAllProducts({ maxPrice: 500 });
      expect(result.products.length).toBe(4);  // Adjusted to 4 products matching the max price filter
      expect(result.products.every(p => p.price <= 500)).toBe(true);
    });

    it('should filter in-stock products', () => {
      const result = productService.getAllProducts({ inStock: 'true' });
      expect(result.products.length).toBe(4);  // Adjusted to 4 in-stock products
      expect(result.products.every(p => p.inStock === true)).toBe(true);
    });

    it('should handle pagination', () => {
      const result = productService.getAllProducts({ limit: 2, offset: 1 });
      expect(result.products.length).toBe(2);
      expect(result.offset).toBe(1);
      expect(result.limit).toBe(2);
    });
  });

  // Testing getProductById method
  describe('getProductById', () => {
    it('should return product by ID', () => {
      const product = productService.getProductById('1');
      expect(product).toHaveProperty('id', '1');
      expect(product).toHaveProperty('name');
    });

    it('should throw error if product not found', () => {
      expect(() => productService.getProductById('999')).toThrow('Product not found');
    });
  });

  // Testing createProduct method
  describe('createProduct', () => {
    it('should create a new product', () => {
      const newProduct = {
        name: 'Table',
        price: 150,
        category: 'furniture',
        stockCount: 8,
      };

      const result = productService.createProduct(newProduct);
      expect(result.product).toHaveProperty('id');
      expect(result.product.name).toBe('Table');
      expect(result.product.category).toBe('furniture');
    });

    it('should throw error if product data is incomplete', () => {
      const incompleteProduct = {
        price: 150,
        category: 'furniture',
      };

      expect(() => productService.createProduct(incompleteProduct)).toThrow('Product must have name, price, and category');
    });
  });

  // Testing updateProduct method
  describe('updateProduct', () => {
    it('should update an existing product', () => {
      const updatedProduct = productService.updateProduct('1', { price: 1200 });
      expect(updatedProduct.product).toHaveProperty('price', 1200);
    });

    it('should throw error if product not found', () => {
      expect(() => productService.updateProduct('999', { price: 1200 })).toThrow('Product not found');
    });
  });

  // Testing deleteProduct method
  describe('deleteProduct', () => {
    it('should delete a product', () => {
      const result = productService.deleteProduct('1');
      expect(result.success).toBe(true);
      expect(result.message).toBe('Product deleted successfully');
    });

    it('should throw error if product not found', () => {
      expect(() => productService.deleteProduct('999')).toThrow('Product not found');
    });
  });

  // Testing getAllCategories method
  describe('getAllCategories', () => {
    it('should return all unique categories', () => {
      const categories = productService.getAllCategories();
      expect(categories.categories.length).toBeGreaterThan(0);
      expect(categories.categories).toContain('electronics');
      expect(categories.categories).toContain('furniture');
    });
  });
});
