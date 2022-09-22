from bs4 import BeautifulSoup
import tqdm
import requests


def check_is_digit(char: str) -> bool:
    try:
        int(char)
        return True
    except Exception:
        return False


def parse_price_from_string(raw_price: str) -> int:
    digit_arr = list(filter(check_is_digit, raw_price))
    return int('0' + ''.join(digit_arr))


def parse_price_from_tag(tag: BeautifulSoup) -> int:
    raw_item = tag.find('div', {'class': 'ListingItemPrice__content'})
    return parse_price_from_string(raw_item.text)


def get_data_on_tags(page: BeautifulSoup) -> (int, int):
    tags = page.find_all('div', {'class': 'ListingItem'})
    total_sum = 0
    for tag in tqdm.tqdm(tags):
        total_sum += parse_price_from_tag(tag)
    return total_sum, len(tags)


def get_data_on_page(page_url: str) -> (int, int):
    with requests.get(page_url) as page:
        page.encoding = 'utf-8'
        return get_data_on_tags(BeautifulSoup(page.text, 'lxml'))


def transform_final_price(price: float) -> str:
    price = int(round(price))
    price_mil = price // (10 ** 6)
    price_thd = price // (10 ** 3) % (10 ** 3)
    price_sml = price % (10 ** 3)

    price = ''
    price += str(price_mil) + ' ' if price_mil != 0 else ''
    price += str(price_thd) + ' ' if price_thd != 0 else ''
    price += str(price_sml) + ' ' if price_sml != 0 else ''
    return price.strip()


def get_data_fully() -> None:
    url = input('Put here your url: ')
    total_sum, total_count = get_data_on_page(url)
    print(f'There is {total_count} cars on your page')
    avg = total_sum / max(total_count, 1)
    print(f'Average price: ~{transform_final_price(avg)}')


if __name__ == '__main__':
    get_data_fully()
