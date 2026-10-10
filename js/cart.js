/**
 * Red Agro - Global Shopping Cart System
 * Manages cart state in localStorage and updates UI badges across all pages
 */

(function () {
  const CART_STORAGE_KEY = 'red_agro_cart_v1';
  const COUPON_STORAGE_KEY = 'red_agro_coupon_v1';

  // Seed default cart items if user has never visited
  const DEFAULT_SEED_ITEMS = [
    {
      id: 'honey',
      name: 'সুন্দরবনের খাঁটি মধু',
      size: '500g Jar',
      price: 450,
      quantity: 1,
      image: 'images/farm-foods.jpg',
      category: 'ফার্মের খাবার'
    },
    {
      id: 'vermicompost',
      name: 'প্রিমিয়াম ভার্মিকম্পোস্ট সার',
      size: '5kg Bag',
      price: 280,
      quantity: 2,
      image: 'images/gardening.jpg',
      category: 'চাষের সরঞ্জাম'
    }
  ];

  function getCart() {
    try {
      const stored = localStorage.getItem(CART_STORAGE_KEY);
      if (stored === null) {
        // First visit: initialize with seed items
        localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(DEFAULT_SEED_ITEMS));
        return [...DEFAULT_SEED_ITEMS];
      }
      return JSON.parse(stored) || [];
    } catch (e) {
      console.error('Error reading cart from localStorage', e);
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(cart));
      updateCartBadges();
      window.dispatchEvent(new CustomEvent('cartUpdated', { detail: { cart } }));
    } catch (e) {
      console.error('Error saving cart to localStorage', e);
    }
  }

  function addToCart(item, qty = 1, showToast = true) {
    const cart = getCart();
    const existingIndex = cart.findIndex(i => i.id === item.id && (i.size || '') === (item.size || ''));

    if (existingIndex > -1) {
      cart[existingIndex].quantity += qty;
    } else {
      cart.push({
        id: item.id,
        name: item.name,
        size: item.size || 'স্ট্যান্ডার্ড',
        price: parseInt(item.price, 10) || 0,
        quantity: qty,
        image: item.image || 'images/farm-foods.jpg',
        category: item.category || 'পণ্য'
      });
    }

    saveCart(cart);

    if (showToast) {
      showCartToast(`${item.name} কার্টে যোগ করা হয়েছে!`);
    }
  }

  function updateQuantity(id, delta, size = null) {
    const cart = getCart();
    const index = cart.findIndex(i => i.id === id && (size === null || (i.size || '') === size));
    if (index > -1) {
      cart[index].quantity += delta;
      if (cart[index].quantity <= 0) {
        cart.splice(index, 1);
      }
      saveCart(cart);
    }
  }

  function removeFromCart(id, size = null) {
    let cart = getCart();
    cart = cart.filter(i => !(i.id === id && (size === null || (i.size || '') === size)));
    saveCart(cart);
  }

  function clearCart() {
    saveCart([]);
  }

  function getCartItemCount() {
    const cart = getCart();
    return cart.reduce((total, item) => total + (item.quantity || 0), 0);
  }

  function getCartSubtotal() {
    const cart = getCart();
    return cart.reduce((total, item) => total + ((item.price || 0) * (item.quantity || 0)), 0);
  }

  function updateCartBadges() {
    const count = getCartItemCount();
    const badges = document.querySelectorAll('.cart-badge, .cart-count');
    badges.forEach(badge => {
      badge.textContent = count;
      if (count > 0) {
        badge.classList.remove('hidden');
        badge.style.display = 'inline-flex';
      } else {
        badge.classList.add('hidden');
        badge.style.display = 'none';
      }
    });
  }

  function showCartToast(message) {
    let toast = document.getElementById('cart-floating-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'cart-floating-toast';
      toast.className = 'fixed top-20 right-4 z-50 transform transition-all duration-300 translate-y-[-20px] opacity-0 pointer-events-none';
      document.body.appendChild(toast);
    }

    toast.innerHTML = `
      <div class="bg-gray-900 text-white px-4 py-3 rounded-2xl shadow-2xl flex items-center gap-3 border border-gray-700/60 pointer-events-auto">
        <div class="w-8 h-8 rounded-full bg-primary-600 flex items-center justify-center flex-shrink-0">
          <i class="fa-solid fa-check text-white text-xs"></i>
        </div>
        <div class="text-xs">
          <p class="font-bold bangla text-white">${message}</p>
          <p class="text-gray-400 bangla text-[11px] mt-0.5">কার্ট দেখতে নিচে ক্লিক করুন</p>
        </div>
        <a href="cart.html" class="ml-2 bg-primary-600 hover:bg-primary-500 text-white text-xs px-3 py-1.5 rounded-xl font-bold bangla transition-colors flex items-center gap-1">
          কার্ট দেখুন <i class="fa-solid fa-arrow-right text-[10px]"></i>
        </a>
      </div>
    `;

    // Animate in
    setTimeout(() => {
      toast.classList.remove('translate-y-[-20px]', 'opacity-0', 'pointer-events-none');
    }, 10);

    // Auto animate out after 3.5s
    if (window._cartToastTimer) clearTimeout(window._cartToastTimer);
    window._cartToastTimer = setTimeout(() => {
      toast.classList.add('translate-y-[-20px]', 'opacity-0', 'pointer-events-none');
    }, 3500);
  }

  // Expose globally
  window.RedAgroCart = {
    getCart,
    saveCart,
    addToCart,
    updateQuantity,
    removeFromCart,
    clearCart,
    getCartItemCount,
    getCartSubtotal,
    updateCartBadges,
    showCartToast,
    CART_STORAGE_KEY,
    COUPON_STORAGE_KEY
  };

  // Initialize badges on DOM ready and storage changes
  document.addEventListener('DOMContentLoaded', updateCartBadges);
  window.addEventListener('storage', updateCartBadges);
})();
