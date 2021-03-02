'''translate'''
'''抓取图片'''

import urllib.request
import os


def get_page(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    req.add_header('Cookie', '_ga=GA1.2.1492311372.1612788374; _gid=GA1.2.2081788341.1612788374; BAIDU_SSP_lcr=https://www.baidu.com/link?url=vx6VPb_sJibLi_2Y33FKiSoFRqVj-oRxGub9zx1hbpK&wd=&eqid=e91b76a6000e52ae0000000560213292; __gads=ID=04085ae5704d4ecb-221b8520f7c500c1:T=1612788373:RT=1612788373:S=ALNI_Mae8cBBDYPo-NpgGmm0oyN-Fl9fCg; gif-click-load=on; nsfw-click-load=on; PHPSESSID=dvfp0p33jvegl1qrjvpm5ssi6i')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    req.add_header('Host', 'jandan.net')
    print(url)
    response = urllib.request.urlopen(url)
    print(response)
    html = response.read().decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    print(html[a:b])

    exit()
def find_images(url):
    pass


def save_images(folder, image_adders):
    pass


def download_img(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        print(page_url)
        img_addrs = find_images(page_url)
        save_images(folder, img_addrs)


if __name__ == '__main__':
    download_img()
