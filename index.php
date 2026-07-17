<?php
/**
 * Main template file.
 *
 * This theme only provides the landing page template-behind-the-chair.php.
 */
get_header(); ?>
<main id="primary" class="site-main">
    <div class="container">
        <?php
        if ( have_posts() ) :
            while ( have_posts() ) :
                the_post();
                the_content();
            endwhile;
        else :
            echo '<p>' . esc_html__( 'No posts found.', 'silverhairstudio' ) . '</p>';
        endif;
        ?>
    </div>
</main>
<?php
get_footer();
