import requests
import pandas as pd

author_dict = {
    1: "ashokfotography",
    39: "Priya",
    2: "tno"
}

cate_res = requests.get('https://thenewsoutlook.com/wp-json/wp/v2/categories?page=1&per_page=100')
cat_data = cate_res.json()


data_list = []
total_count = 0
for page_num in range(1, 13):
    response = requests.get(f'https://thenewsoutlook.com/wp-json/wp/v2/posts?page={page_num}&per_page=100')
    print(f'Current Page is ... {page_num}')
    if response.ok:
        data = response.json()
        total_count += len(data)
        for item in data:
            post_id = item['id']
            pub_date = item['date']
            author = item['author']
            author_name = author_dict[item['author']]
            slug = item['slug']
            status = item['status']
            class_list = ", ".join(item['class_list'])
            post_type = item['type']
            url = item['link']
            title = item['title']['rendered']
            meta_content = item['content']['rendered']
            rendered_content = item['excerpt']['rendered']
            category = item['categories']
            category_name = []
            category_slug = []
            for cate_id in category:
                cate_matched_item = [a for a in cat_data if a['id'] == cate_id]
                category_name.append(cate_matched_item[0]['name'])
                category_slug.append(cate_matched_item[0]['slug'])
            img_url = item['jetpack_featured_media_url']
            data_dict = {
                "post_id": post_id,
                "pub_date": pub_date,
                "slug": slug,
                "status": status,
                "author": author,
                "author_name": author_name,
                "post_type": post_type,
                "url": url,
                "title": title,
                "meta_content": meta_content,
                "rendered_content": rendered_content,
                "category": category,
                "category_name": ', '.join(category_name),
                "category_slug": ', '.join(category_slug),
                "img_url": img_url,
                "class_list": class_list,
            }
            data_list.append(data_dict)
        df = pd.DataFrame(data_list)
        df.to_csv('tno.csv')


print(f'Total data....{total_count}')


# read_data = pd.read_csv('tno.csv')
# for i, row in read_data.iterrows():
#     print(row['meta_content'])
