import re
import os

html_path = r'c:\laragon\www\wp\test3\wp-content\themes\silverhairstudio\BehindTheChair.html'
php_path = r'c:\laragon\www\wp\test3\wp-content\themes\silverhairstudio\template-behind-the-chair.php'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Strip Content Security Policy meta tags to allow WordPress core assets to load
content = re.sub(r'<meta http-equiv=["\']?content-security-policy["\']?[^>]*>', '', content, flags=re.IGNORECASE)


# 1. Image Replacements mapping index to ACF field name
img_field_map = {
    0: 'site_logo',
    4: 'hero_background',
    5: 'partner_logo_1',
    6: 'partner_logo_2',
    7: 'partner_logo_3',
    8: 'partner_logo_4',
    9: 'partner_logo_5',
    10: 'showcase_image_1',
    11: 'showcase_image_2',
    12: 'showcase_image_3',
    13: 'showcase_image_4',
    14: 'showcase_image_5',
    15: 'showcase_image_6',
    16: 'showcase_image_7',
    17: 'showcase_image_8',
    18: 'showcase_image_9',
    19: 'secondary_image',
    20: 'about_background'
}

img_index = 0
def replace_img_src(match):
    global img_index
    tag_content = match.group(0)
    src_match = re.search(r'src=["\']?([^"\'\s>]+)["\']?', tag_content)
    
    if not src_match:
        img_index += 1
        return tag_content
        
    src_val = src_match.group(1)
    
    if img_index in img_field_map:
        field_name = img_field_map[img_index]
        token = f'##TOKEN_IMG_{field_name.upper()}##'
        tag_content = tag_content.replace(src_val, token)
        
    img_index += 1
    return tag_content

# Match all data:image/ or base64 sources
content = re.sub(r'src=["\']?(data:image/[^"\'\s>]+)["\']?', replace_img_src, content)
content = re.sub(r'src=["\']?(data:image/webp;base64,[^"\'\s>]+)["\']?', replace_img_src, content)

# 2. Map original texts to unique tokens
text_to_token = [
    # Hero description
    ("More than a hair salon, we create experiences and style your hair with care and skill made just for you. More than a client, you’re a valued friend we’re always happy to welcome back!", "##TOKEN_HERO_DESC##"),
    
    # About text
    ("Behind The Chair được thành lập từ tháng 10/2020. \"Phía sau chiếc ghế\" thể hiện triết lý làm nghề của chúng tôi : phía sau mỗi mái tóc đẹp là một stylist tận tâm, giàu kinh nghiệm và đầy đam mê. Đội ngũ được tuyển chọn kỹ lưỡng, dẫn dắt bởi chuyên gia tạo mẫu tóc :", "##TOKEN_ABOUT_TEXT##"),
    
    # Founder Title Sub
    ("&amp; Đại sứ thương hiệu Brazilian Bond Builder.", "##TOKEN_FOUNDER_TITLE_SUB##"),
    ("& Đại sứ thương hiệu Brazilian Bond Builder.", "##TOKEN_FOUNDER_TITLE_SUB##"),
    
    # Founder Title
    ("Founder Behind The Chair ", "##TOKEN_FOUNDER_TITLE##"),
    ("Founder Behind The Chair", "##TOKEN_FOUNDER_TITLE##"),
    
    # Top Bar Text
    ("L'Oreal Pro Salon &amp; Trusted brands only", "##TOKEN_TOP_BAR##"),
    ("L'Oreal Pro Salon & Trusted brands only", "##TOKEN_TOP_BAR##"),
    
    # Partner Title
    ("THƯƠNG HIỆU <em>ĐỒNG HÀNH</em>", "##TOKEN_PARTNER_TITLE##"),
    ("THƯƠNG HIỆU &lt;em&gt;ĐỒNG HÀNH&lt;/em&gt;", "##TOKEN_PARTNER_TITLE##"),
    
    # Booking
    ("https://l.facebook.com/l.php?u=https://m.me/btc.hairsalon", "##TOKEN_BOOKING_URL##"),
    ("https://m.me/btc.hairsalon", "##TOKEN_BOOKING_URL##"),
    ("Đặt lịch", "##TOKEN_BOOKING_TEXT##"),
    
    # Instagram Follow Text
    ("Hãy theo dõi chúng tôi tại Instagram để xem nhiều hơn", "##TOKEN_INSTAGRAM_TEXT##"),
    
    # Social URLs
    ("https://www.tiktok.com/@btc.hairstudio1", "##TOKEN_TIKTOK_URL##"),
    ("https://www.instagram.com/btc.hairstudio/", "##TOKEN_INSTAGRAM_URL##"),
    ("https://www.facebook.com/btc.hairsalon", "##TOKEN_FACEBOOK_URL##"),
    
    # Instagram Handle
    ("@btc.hairstudio", "##TOKEN_INSTAGRAM_HANDLE##"),
    
    # Contact Footer
    ("LIÊN HỆ VỚI BEHIND THE CHAIR", "##TOKEN_CONTACT_TITLE##"),
    ("407/3 Lê Văn Sỹ, Phường 12, Quận 3, TP.HCM (không chi nhánh)", "##TOKEN_ADDRESS_DETAIL##"),
    ("Địa chỉ", "##TOKEN_ADDRESS_TITLE##"),
    
    # Hotline / Phone
    ("Hotline : 0905 094 600", "##TOKEN_STATIC_HOTLINE##"),
    ("0905094600", "##TOKEN_HOTLINE_NUMBER##"),
    ("0905 094 600", "##TOKEN_HOTLINE_NUMBER##"),

    
    # Satisfaction Quote
    ("“Our happiness come from making you feel truly satisfied”", "“OUR HAPPINESS COME FROM MAKING YOU FEEL TRULY SATISFIED”"),

    
    # Hero Title
    ("CRAFTED WITH CARE", "##TOKEN_HERO_TITLE##"),
    
    # About Title
    ("VỀ CHÚNG TÔI", "##TOKEN_ABOUT_TITLE##"),
    
    # Founder Name
    ("Mai Huy Hoàng", "##TOKEN_FOUNDER_NAME##"),
    
    # Services Title
    ("DỊCH VỤ", "##TOKEN_SERVICES_TITLE##"),
    ("CỦA CHÚNG TÔI", "##TOKEN_SERVICES_TITLE_SUB##"),
    
    # Explore Title
    ("MORE TO EXPLORE", "##TOKEN_EXPLORE_TITLE##"),
]

# Run string-to-token replacements
for old_txt, token in text_to_token:
    content = content.replace(old_txt, token)

# 3. Expand the tokens into their corresponding PHP blocks
# Note: we use double backslashes for L\'Oreal in python strings to output a single backslash in PHP
token_to_php = {
    "##TOKEN_STATIC_HOTLINE##": "Hotline: 0905 094 600",
    "##TOKEN_TOP_BAR##": "<?php echo esc_html(get_field('top_bar_text') ?: 'L\\\'Oreal Pro Salon & Trusted brands only'); ?>",
    "##TOKEN_HOTLINE_NUMBER##": "<?php echo esc_html(get_field('hotline_number') ?: '0905094600'); ?>",

    "##TOKEN_HERO_TITLE##": "<?php echo esc_html(get_field('hero_title') ?: 'CRAFTED WITH CARE'); ?>",
    "##TOKEN_HERO_DESC##": "<?php echo esc_html(get_field('hero_description') ?: 'More than a hair salon, we create experiences and style your hair with care and skill made just for you. More than a client, you’re a valued friend we’re always happy to welcome back!'); ?>",
    "##TOKEN_BOOKING_TEXT##": "<?php echo esc_html(get_field('booking_text') ?: 'Đặt lịch'); ?>",
    "##TOKEN_BOOKING_URL##": "<?php echo esc_url(get_field('booking_url') ?: 'https://m.me/btc.hairsalon'); ?>",
    "##TOKEN_ABOUT_TITLE##": "<?php echo esc_html(get_field('about_title') ?: 'VỀ CHÚNG TÔI'); ?>",
    "##TOKEN_ABOUT_TEXT##": "<?php echo esc_html(get_field('about_text') ?: 'Behind The Chair được thành lập từ tháng 10/2020. \"Phía sau chiếc ghế\" thể hiện triết lý làm nghề của chúng tôi : phía sau mỗi mái tóc đẹp là một stylist tận tâm, giàu kinh nghiệm và đầy đam mê. Đội ngũ được tuyển chọn kỹ lưỡng, dẫn dắt bởi chuyên gia tạo mẫu tóc :'); ?>",
    "##TOKEN_FOUNDER_NAME##": "<?php echo esc_html(get_field('founder_name') ?: 'Mai Huy Hoàng'); ?>",
    "##TOKEN_FOUNDER_TITLE##": "<?php echo esc_html(get_field('founder_title') ?: 'Founder Behind The Chair'); ?>",
    "##TOKEN_FOUNDER_TITLE_SUB##": "<?php echo esc_html(get_field('founder_title_sub') ?: '& Đại sứ thương hiệu Brazilian Bond Builder.'); ?>",
    "##TOKEN_PARTNER_TITLE##": "<?php echo wp_kses_post(get_field('partner_title') ?: 'THƯƠNG HIỆU <em>ĐỒNG HÀNH</em>'); ?>",
    "##TOKEN_SERVICES_TITLE##": "<?php $s_title = get_field('services_title') ?: 'DỊCH VỤ'; echo esc_html($s_title === 'DỊCH VỤ CỦA CHÚNG TÔI' ? 'DỊCH VỤ' : $s_title); ?>",
    "##TOKEN_SERVICES_TITLE_SUB##": "<?php echo esc_html(get_field('services_title_sub') ?: 'CỦA CHÚNG TÔI'); ?>",
    "##TOKEN_EXPLORE_TITLE##": "<?php echo esc_html(get_field('explore_title') ?: 'MORE TO EXPLORE'); ?>",
    "##TOKEN_INSTAGRAM_HANDLE##": "<?php echo esc_html(get_field('instagram_handle') ?: '@btc.hairstudio'); ?>",
    "##TOKEN_INSTAGRAM_URL##": "<?php echo esc_url(get_field('instagram_url') ?: 'https://www.instagram.com/btc.hairstudio/'); ?>",
    "##TOKEN_INSTAGRAM_TEXT##": "<?php echo esc_html(get_field('instagram_text') ?: 'Hãy theo dõi chúng tôi tại Instagram để xem nhiều hơn'); ?>",
    "##TOKEN_TIKTOK_URL##": "<?php echo esc_url(get_field('tiktok_url') ?: 'https://www.tiktok.com/@btc.hairstudio1'); ?>",
    "##TOKEN_FACEBOOK_URL##": "<?php echo esc_url(get_field('facebook_url') ?: 'https://www.facebook.com/btc.hairsalon'); ?>",
    "##TOKEN_CONTACT_TITLE##": "<?php echo esc_html(get_field('contact_title') ?: 'LIÊN HỆ VỚI BEHIND THE CHAIR'); ?>",
    "##TOKEN_ADDRESS_TITLE##": "<?php echo esc_html(get_field('address_title') ?: 'Địa chỉ'); ?>",
    "##TOKEN_ADDRESS_DETAIL##": "<?php echo esc_html(get_field('address_detail') ?: '407/3 Lê Văn Sỹ, Phường 12, Quận 3, TP.HCM (không chi nhánh)'); ?>",
}

for token, php_code in token_to_php.items():
    content = content.replace(token, php_code)

# 4. Expand Image Tokens dynamically with original base64 strings preserved as fallback
with open(html_path, 'r', encoding='utf-8') as f_orig:
    orig_content = f_orig.read()

img_tags_orig = re.findall(r'<img[^>]+>', orig_content, re.IGNORECASE)
orig_src_vals = []
for tag in img_tags_orig:
    src_match = re.search(r'src=["\']?([^"\'\s>]+)["\']?', tag)
    if src_match:
        orig_src_vals.append(src_match.group(1))

print(f"Collected {len(orig_src_vals)} original images.")

for idx, field_name in img_field_map.items():
    token = f'##TOKEN_IMG_{field_name.upper()}##'
    if idx < len(orig_src_vals):
        fallback_src = orig_src_vals[idx]
        php_code = f'<?php $img_{field_name} = get_field("{field_name}"); echo $img_{field_name} ? esc_url($img_{field_name}["url"]) : "{fallback_src}"; ?>'
        content = content.replace(token, php_code)

# 5. Prepend WordPress Page Template Header
header = """<?php
/*
Template Name: Behind The Chair Landing Page
*/
?>
"""

final_content = header + content

with open(php_path, 'w', encoding='utf-8') as f_out:
    f_out.write(final_content)

print("Template conversion complete! Saved to template-behind-the-chair.php")
