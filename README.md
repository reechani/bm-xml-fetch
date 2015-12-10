# bm-xml-fetch

Python script that fetches the xml of all products and checks for a given tag to match and get that product into a list.
The script automatically get's how many product pages there are, and there is a paus of currently 0.15s between each product
page fetch. This it to not overload the servers. I advise not to remove it or decrease it too much, that could result in 
the target site going down due to overload.
The products are returned as a JSON object into the file given in the argument.
The repo includes some html/css (I'm ashamed by the inline css) and javascript to show the results, but this you can of
course write yourself as well.

My javascript includes:
- Ajax call to fetch the JSON products
- Sorting of the products by name
- Comparing 2 JSON products lists with eachother - in this case I manually rename the file to *-old.php when running the
script again, so that I can see what items might have been added and removed since last time I ran it.

## Arguments
```
-t [tagname]
```
Required. Specifies the tag to search for in the xml <tags>.

```
-f [filename]
```
Required. The file to save the result into. The result is outputed as a JSON string.

```
--us
```
Optional. Will query the US site instead of the AUS (international).

### Example
```
./bm-xml.py -f museum-dec-2015.php -t Museum_Sale_Dec_2015
```
## index.html

All content here is loaded automatically by the javscript.

## main.js

You need to change the following lines to show the files correctly:
- `files` - The 2 files to be loaded, `old` and `new`. These are the files that are compared.
- `off` - If there is an expected general discount, this can be changed. For example set it to `0.3` for 30% off.
- `title` - The title of the page.
- `tag` - The tag used to get the products.

## Product object

The product name acts as the key for the product. The object has the following properties:
- `url` - URL to the product page
- `img` - Product image
- `price` - The product price

Example:
```
"Candy Hearts Pencil Skirt": {
  "url": "http://blackmilkclothing.com/collections/all/products/candy-hearts-pencil-skirt",
  "price": "60.00",
  "img": "https://cdn.shopify.com/s/files/1/0115/5832/products/150825-Candy-WifeySkirt-WEB-1.jpg?v=1440039886"
}
```

## TODO
- Add error handling again
- Automatically create the html and js (optional) from templates instead of outputing into json or have this as optional argument to output into templates instead of json
- Save images locally (maybe)
