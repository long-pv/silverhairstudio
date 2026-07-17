<?php
/**
 * Silver Hair Studio functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package Silver_Hair_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly.
}

/**
 * Setup Theme
 */
function silverhairstudio_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
}
add_action( 'after_setup_theme', 'silverhairstudio_setup' );

/**
 * Enqueue scripts and styles.
 */
function silverhairstudio_scripts() {
    wp_enqueue_style( 'silverhairstudio-main-style', get_template_directory_uri() . '/assets/css/main.css', array(), time() );
    wp_enqueue_style( 'silverhairstudio-mobile-style', get_template_directory_uri() . '/assets/css/mobile-overrides.css', array('silverhairstudio-main-style'), time() );
}
add_action( 'wp_enqueue_scripts', 'silverhairstudio_scripts' );


/**
 * Register ACF Fields via PHP
 */
if ( function_exists('acf_add_local_field_group') ) {

    acf_add_local_field_group(array(
        'key' => 'group_behind_the_chair',
        'title' => 'Behind The Chair Page Fields',
        'fields' => array(
            // Header Group
            array(
                'key' => 'field_site_logo',
                'label' => 'Site Logo',
                'name' => 'site_logo',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_top_bar_text',
                'label' => 'Top Bar Text',
                'name' => 'top_bar_text',
                'type' => 'text',
                'default_value' => 'L\'Oreal Pro Salon & Trusted brands only',
            ),
            array(
                'key' => 'field_hotline_number',
                'label' => 'Hotline Number',
                'name' => 'hotline_number',
                'type' => 'text',
                'default_value' => '0905094600',
            ),
            // Hero Section
            array(
                'key' => 'field_hero_background',
                'label' => 'Hero Background Image',
                'name' => 'hero_background',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_hero_title',
                'label' => 'Hero Title',
                'name' => 'hero_title',
                'type' => 'text',
                'default_value' => 'CRAFTED WITH CARE',
            ),
            array(
                'key' => 'field_hero_description',
                'label' => 'Hero Description',
                'name' => 'hero_description',
                'type' => 'textarea',
                'default_value' => 'More than a hair salon, we create experiences and style your hair with care and skill made just for you...',
            ),
            array(
                'key' => 'field_booking_text',
                'label' => 'Booking Button Text',
                'name' => 'booking_text',
                'type' => 'text',
                'default_value' => 'Đặt lịch',
            ),
            array(
                'key' => 'field_booking_url',
                'label' => 'Booking Button URL',
                'name' => 'booking_url',
                'type' => 'text',
                'default_value' => 'https://m.me/btc.hairsalon',
            ),
            // About Section
            array(
                'key' => 'field_about_title',
                'label' => 'About Title',
                'name' => 'about_title',
                'type' => 'text',
                'default_value' => 'VỀ CHÚNG TÔI',
            ),
            array(
                'key' => 'field_about_text',
                'label' => 'About Text',
                'name' => 'about_text',
                'type' => 'textarea',
                'default_value' => 'Behind The Chair được thành lập từ tháng 10/2020. "Phía sau chiếc ghế" thể hiện triết lý làm nghề của chúng tôi...',
            ),
            array(
                'key' => 'field_founder_name',
                'label' => 'Founder Name',
                'name' => 'founder_name',
                'type' => 'text',
                'default_value' => 'Mai Huy Hoàng',
            ),
            array(
                'key' => 'field_founder_title',
                'label' => 'Founder Title',
                'name' => 'founder_title',
                'type' => 'text',
                'default_value' => 'Founder Behind The Chair & Đại sứ thương hiệu Brazilian Bond Builder.',
            ),
            // Partner Section
            array(
                'key' => 'field_partner_title',
                'label' => 'Partner Section Title',
                'name' => 'partner_title',
                'type' => 'text',
                'default_value' => 'THƯƠNG HIỆU ĐỒNG HÀNH',
            ),
            array(
                'key' => 'field_partner_logo_1',
                'label' => 'Partner Logo 1',
                'name' => 'partner_logo_1',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_partner_logo_2',
                'label' => 'Partner Logo 2',
                'name' => 'partner_logo_2',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_partner_logo_3',
                'label' => 'Partner Logo 3',
                'name' => 'partner_logo_3',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_partner_logo_4',
                'label' => 'Partner Logo 4',
                'name' => 'partner_logo_4',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_partner_logo_5',
                'label' => 'Partner Logo 5',
                'name' => 'partner_logo_5',
                'type' => 'image',
                'return_format' => 'array',
            ),
            // Services
            array(
                'key' => 'field_services_title',
                'label' => 'Services Title',
                'name' => 'services_title',
                'type' => 'text',
                'default_value' => 'DỊCH VỤ',
            ),
            array(
                'key' => 'field_services_title_sub',
                'label' => 'Services Title Sub',
                'name' => 'services_title_sub',
                'type' => 'text',
                'default_value' => 'CỦA CHÚNG TÔI',
            ),
            // Showcase Images 1-9
            array(
                'key' => 'field_showcase_image_1',
                'label' => 'Showcase Image 1',
                'name' => 'showcase_image_1',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_2',
                'label' => 'Showcase Image 2',
                'name' => 'showcase_image_2',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_3',
                'label' => 'Showcase Image 3',
                'name' => 'showcase_image_3',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_4',
                'label' => 'Showcase Image 4',
                'name' => 'showcase_image_4',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_5',
                'label' => 'Showcase Image 5',
                'name' => 'showcase_image_5',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_6',
                'label' => 'Showcase Image 6',
                'name' => 'showcase_image_6',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_7',
                'label' => 'Showcase Image 7',
                'name' => 'showcase_image_7',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_8',
                'label' => 'Showcase Image 8',
                'name' => 'showcase_image_8',
                'type' => 'image',
                'return_format' => 'array',
            ),
            array(
                'key' => 'field_showcase_image_9',
                'label' => 'Showcase Image 9',
                'name' => 'showcase_image_9',
                'type' => 'image',
                'return_format' => 'array',
            ),
            // Explore Title
            array(
                'key' => 'field_explore_title',
                'label' => 'Explore Title',
                'name' => 'explore_title',
                'type' => 'text',
                'default_value' => 'MORE TO EXPLORE',
            ),
            // Social
            array(
                'key' => 'field_instagram_handle',
                'label' => 'Instagram Handle',
                'name' => 'instagram_handle',
                'type' => 'text',
                'default_value' => '@btc.hairstudio',
            ),
            array(
                'key' => 'field_instagram_url',
                'label' => 'Instagram URL',
                'name' => 'instagram_url',
                'type' => 'text',
                'default_value' => 'https://www.instagram.com/btc.hairstudio/',
            ),
            array(
                'key' => 'field_instagram_text',
                'label' => 'Instagram Follow Text',
                'name' => 'instagram_text',
                'type' => 'text',
                'default_value' => 'Hãy theo dõi chúng tôi tại Instagram để xem nhiều hơn',
            ),
            // Contact Footer
            array(
                'key' => 'field_contact_title',
                'label' => 'Contact Section Title',
                'name' => 'contact_title',
                'type' => 'text',
                'default_value' => 'LIÊN HỆ VỚI BEHIND THE CHAIR',
            ),
            array(
                'key' => 'field_address_title',
                'label' => 'Address Label',
                'name' => 'address_title',
                'type' => 'text',
                'default_value' => 'Địa chỉ',
            ),
            array(
                'key' => 'field_address_detail',
                'label' => 'Address Detail',
                'name' => 'address_detail',
                'type' => 'text',
                'default_value' => '407/3 Lê Văn Sỹ, Phường 12, Quận 3, TP.HCM (không chi nhánh)',
            ),
            array(
                'key' => 'field_facebook_url',
                'label' => 'Facebook URL',
                'name' => 'facebook_url',
                'type' => 'text',
                'default_value' => 'https://www.facebook.com/btc.hairsalon',
            ),
            array(
                'key' => 'field_tiktok_url',
                'label' => 'Tiktok URL',
                'name' => 'tiktok_url',
                'type' => 'text',
                'default_value' => 'https://www.tiktok.com/@btc.hairstudio1',
            ),
        ),
        'location' => array(
            array(
                array(
                    'param' => 'page_template',
                    'operator' => '==',
                    'value' => 'template-behind-the-chair.php',
                ),
            ),
        ),
    ));

}
