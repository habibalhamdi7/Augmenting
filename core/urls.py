from django.urls import path, include
from core.views import PredictionView, Training, about_us, add_to_wishlist, ajax_contact_form, contact, customer_dashboard, index, category_list_view, make_default, order_detail, payment_view, privacy_policy, product_list_view, category_product_list__view, purchase_guide, remove_wishlist, terms_of_service, vendor_list_view, vendor_detail_view, product_detail_view, tag_list, ajax_add_review, search_view, filter_product, add_to_cart, cart_view, delete_item_from_cart, update_cart, checkout_view, payment_completed_view, payment_failed_view, wishlist_view
from django import views

app_name = "core"

urlpatterns = [
    # Homepage
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),
    # Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),
    # Vendor
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),
    # Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
    # Add Review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),
    # Search
    path("search/", search_view, name="search"),
    # Filter product URL
    path("filter-products/", filter_product, name="filter-product"),
    # Add to Cart URL
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    # Cart Page URL
    path("cart/", cart_view, name="cart"),
    # Delete Item From Cart URL
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    # Update Cart URL
    path("update-cart/", update_cart, name="update-cart"),
    # Checkout URL
    path("checkout/", checkout_view, name="checkout"),
    # PayPal URL
    path("paypal/", include('paypal.standard.ipn.urls')),
    # Checkout URL
    path("checkout/", checkout_view, name="checkout"),
    # Payment Midtrans URL
     path('payment/', payment_view, name='payment'),
    # Payment Successfull URL
    path("payment-completed/", payment_completed_view, name="payment-completed"),
    # Payment Failed URL
    path("payment-failed/", payment_failed_view, name="payment-failed"),
    # Dashboard URL
    path("dashboard/", customer_dashboard, name="dashboard"),
    # Order Detail URL
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),
    # Making Address Default URL
    path("make-default-address/", make_default, name="make-default-address"),
    # wishlist page URL
    path("wishlist/", wishlist_view, name="wishlist"),
    # adding to wishlist URL
    path("add-to-wishlist/", add_to_wishlist, name="add-to-wishlist"),
     # Removing from wishlist URL
    path("remove-from-wishlist/", remove_wishlist, name="remove-from-wishlist"),

    path("contact/", contact, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),

    #Price Genteng Prediction
    path("training/", Training.as_view(), name="training"),
    path("price/", PredictionView.as_view(), name="price-genteng-prediction"),

    path("about_us/", about_us, name="about-us"),
    path("purchase_guide/", purchase_guide, name="purchase_guide"),
    path("privacy_policy/", privacy_policy, name="privacy_policy"),
    path("terms_of_service/", terms_of_service, name="terms_of_service"),
]