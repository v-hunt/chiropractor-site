from wagtail.wagtailimages.formats import (
    Format,
    register_image_format,
    unregister_image_format
)


register_image_format(
    Format('small_image_left', 'Small Image Left', 'richtext-image small_image_left left', 'width-540')
)

unregister_image_format('left')
unregister_image_format('right')
