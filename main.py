from producer_raw_recipies import connect_kafka_producer, get_recipes, publish_message


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
    
    all_recipes = get_recipes(headers)

    if len(all_recipes) > 0:
        for recipe in all_recipes:
            publish_message(connect_kafka_producer(), 'raw_recipes', 'raw', recipe.strip())
            # publish_message(connect_kafka_producer(), 'raw_recipes', 'foobar', b'some_message_bytes')