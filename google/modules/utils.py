from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

from future import standard_library

standard_library.install_aliases()
from builtins import range
from past.utils import old_div
import time
from selenium import webdriver
import urllib.request
import urllib.error
import urllib.parse
from functools import wraps
# import requests
from urllib.parse import urlencode
from fake_useragent import UserAgent
import sys


class AreaError(KeyError):
    pass


area_dict = {
    'com': u"www.google.com/search?",
    'is': 'www.google.is/search?',
    'dk': 'www.google.dk/search?',
    'no': 'www.google.no/search?',
    'se': 'www.google.se/search?',
    'fi': 'www.google.fi/search?',
    'ee': 'www.google.ee/search?',
    'lv': 'www.google.lv/search?',
    'lt': 'www.google.lt/search?',
    'ie': 'www.google.ie/search?',
    'uk': 'www.google.co.uk/search?',
    'gg': 'www.google.gg/search?',
    'je': 'www.google.je/search?',
    'im': 'www.google.im/search?',
    'fr': 'www.google.fr/search?',
    'nl': 'www.google.nl/search?',
    'be': 'www.google.be/search?',
    'lu': 'www.google.lu/search?',
    'de': 'www.google.de/search?',
    'at': 'www.google.at/search?',
    'ch': 'www.google.ch/search?',
    'li': 'www.google.li/search?',
    'pt': 'www.google.pt/search?',
    'es': 'www.google.es/search?',
    'gi': 'www.google.com.gi/search?',
    'ad': 'www.google.ad/search?',
    'it': 'www.google.it/search?',
    'mt': 'www.google.com.mt/search?',
    'sm': 'www.google.sm/search?',
    'gr': 'www.google.gr/search?',
    'ru': 'www.google.ru/search?',
    'by': 'www.google.com.by/search?',
    'ua': 'www.google.com.ua/search?',
    'pl': 'www.google.pl/search?',
    'cz': 'www.google.cz/search?',
    'sk': 'www.google.sk/search?',
    'hu': 'www.google.hu/search?',
    'si': 'www.google.si/search?',
    'hr': 'www.google.hr/search?',
    'ba': 'www.google.ba/search?',
    'me': 'www.google.me/search?',
    'rs': 'www.google.rs/search?',
    'mk': 'www.google.mk/search?',
    'bg': 'www.google.bg/search?',
    'ro': 'www.google.ro/search?',
    'md': 'www.google.md/search?',
    'hk': 'www.google.com.hk/search?',
    'mn': 'www.google.mn/search?',
    'kr': 'www.google.co.kr/search?',
    'jp': 'www.google.co.jp/search?',
    'vn': 'www.google.com.vn/search?',
    'la': 'www.google.la/search?',
    'kh': 'www.google.com.kh/search?',
    'th': 'www.google.co.th/search?',
    'my': 'www.google.com.my/search?',
    'sg': 'www.google.com.sg/search?',
    'bn': 'www.google.com.bn/search?',
    'ph': 'www.google.com.ph/search?',
    'id': 'www.google.co.id/search?',
    'tp': 'www.google.tp/search?',
    'kz': 'www.google.kz/search?',
    'kg': 'www.google.kg/search?',
    'tj': 'www.google.com.tj/search?',
    'uz': 'www.google.co.uz/search?',
    'tm': 'www.google.tm/search?',
    'af': 'www.google.com.af/search?',
    'pk': 'www.google.com.pk/search?',
    'np': 'www.google.com.np/search?',
    'in': 'www.google.co.in/search?',
    'bd': 'www.google.com.bd/search?',
    'lk': 'www.google.lk/search?',
    'mv': 'www.google.mv/search?',
    'kw': 'www.google.com.kw/search?',
    'sa': 'www.google.com.sa/search?',
    'bh': 'www.google.com.bh/search?',
    'ae': 'www.google.ae/search?',
    'om': 'www.google.com.om/search?',
    'jo': 'www.google.jo/search?',
    'il': 'www.google.co.il/search?',
    'lb': 'www.google.com.lb/search?',
    'tr': 'www.google.com.tr/search?',
    'az': 'www.google.az/search?',
    'am': 'www.google.am/search?',
    'ls': 'www.google.co.ls/search?',
    'eg': 'www.google.com.eg/search?',
    'ly': 'www.google.com.ly/search?',
    'dz': 'www.google.dz/search?',
    'ma': 'www.google.co.ma/search?',
    'sn': 'www.google.sn/search?',
    'gm': 'www.google.gm/search?',
    'ml': 'www.google.ml/search?',
    'bf': 'www.google.bf/search?',
    'sl': 'www.google.com.sl/search?',
    'ci': 'www.google.ci/search?',
    'gh': 'www.google.com.gh/search?',
    'tg': 'www.google.tg/search?',
    'bj': 'www.google.bj/search?',
    'ne': 'www.google.ne/search?',
    'ng': 'www.google.com.ng/search?',
    'sh': 'www.google.sh/search?',
    'cm': 'www.google.cm/search?',
    'td': 'www.google.td/search?',
    'cf': 'www.google.cf/search?',
    'ga': 'www.google.ga/search?',
    'cg': 'www.google.cg/search?',
    'cd': 'www.google.cd/search?',
    'ao': 'www.google.it.ao/search?',
    'et': 'www.google.com.et/search?',
    'dj': 'www.google.dj/search?',
    'ke': 'www.google.co.ke/search?',
    'ug': 'www.google.co.ug/search?',
    'tz': 'www.google.co.tz/search?',
    'rw': 'www.google.rw/search?',
    'bi': 'www.google.bi/search?',
    'mw': 'www.google.mw/search?',
    'mz': 'www.google.co.mz/search?',
    'mg': 'www.google.mg/search?',
    'sc': 'www.google.sc/search?',
    'mu': 'www.google.mu/search?',
    'zm': 'www.google.co.zm/search?',
    'zw': 'www.google.co.zw/search?',
    'bw': 'www.google.co.bw/search?',
    'na': 'www.google.com.na/search?',
    'za': 'www.google.co.za/search?',
    'au': 'www.google.com.au/search?',
    'nf': 'www.google.com.nf/search?',
    'nz': 'www.google.co.nz/search?',
    'sb': 'www.google.com.sb/search?',
    'fj': 'www.google.com.fj/search?',
    'fm': 'www.google.fm/search?',
    'ki': 'www.google.ki/search?',
    'nr': 'www.google.nr/search?',
    'tk': 'www.google.tk/search?',
    'ws': 'www.google.ws/search?',
    'as': 'www.google.as/search?',
    'to': 'www.google.to/search?',
    'nu': 'www.google.nu/search?',
    'ck': 'www.google.co.ck/search?',
    'do': 'www.google.com.do/search?',
    'tt': 'www.google.tt/search?',
    'co': 'www.google.com.co/search?',
    'ec': 'www.google.com.ec/search?',
    've': 'www.google.co.ve/search?',
    'gy': 'www.google.gy/search?',
    'pe': 'www.google.com.pe/search?',
    'bo': 'www.google.com.bo/search?',
    'py': 'www.google.com.py/search?',
    'br': 'www.google.com.br/search?',
    'uy': 'www.google.com.uy/search?',
    'ar': 'www.google.com.ar/search?',
    'cl': 'www.google.cl/search?',
    'gl': 'www.google.gl/search?',
    'ca': 'www.google.ca/search?',
    'mx': 'www.google.com.mx/search?',
    'gt': 'www.google.com.gt/search?',
    'bz': 'www.google.com.bz/search?',
    'sv': 'www.google.com.sv/search?',
    'hn': 'www.google.hn/search?',
    'ni': 'www.google.com.ni/search?',
    'cr': 'www.google.co.cr/search?',
    'pa': 'www.google.com.pa/search?',
    'bs': 'www.google.bs/search?',
    'cu': 'www.google.com.cu/search?',
    'jm': 'www.google.com.jm/search?',
    'ht': 'www.google.ht/search?'
}


def measure_time(fn):
    def decorator(*args, **kwargs):
        start = time.time()

        res = fn(*args, **kwargs)

        elapsed = time.time() - start
        print(fn.__name__, "took", elapsed, "seconds")

        return res

    return decorator


def _get_search_url(query, page=0, per_page=10, lang='en', area='com',
                    ncr=False, time_period=False, site=False):

    # note: if site is set and ncr=True then change area to proper google domain if exists
    if site:
        query += f" site:{site}"
        domain = site.split(".")[-1]
        if ncr and domain in area_dict:
            area = domain

    params = {
        'q': query.encode('utf8'),
        'start': page * per_page,
        'num': per_page,
        'hl': lang
    }

    time_mapping = {
        'hour': 'qdr:h',
        'week': 'qdr:w',
        'month': 'qdr:m',
        'year': 'qdr:y'
    }

    if time_period and time_period in time_mapping:
        params['tbs'] = time_mapping[time_period]

    if ncr:
        params['gl'] = 'us'  # Geographic Location: US
        params['pws'] = '0'  # 'pws' = '0' disables personalised search
        params['gws_rd'] = 'cr'  # Google Web Server ReDirect: CountRy.

    if area in area_dict:
        url = area_dict[area]
    else:
        raise AreaError('invalid  name,  no area found')

    # @author JuaniFilardo:
    # Workaround to switch between http and https, since this maneuver
    # seems to avoid the 503 error when performing a lot of queries.
    # Weird, but it works.
    protocol = "https://" if int(time.time()) % 2 == 0 else "http://"

    params = urlencode(params)
    url = protocol + url + params

    return url


def get_html(url):
    ua = UserAgent()
    header = ua.random

    try:
        request = urllib.request.Request(url)
        request.add_header("User-Agent", header)
        html = urllib.request.urlopen(request).read()
        return html
    except urllib.error.HTTPError as e:
        print("Error accessing:", url)
        print(e)
        if e.code == 503 and 'CaptchaRedirect' in e.read():
            print("Google is requiring a Captcha. "
                  "For more information check: 'https://support.google.com/websearch/answer/86640'")
        if e.code == 503:
            sys.exit("503 Error: service is currently unavailable. Program will exit.")
        return None
    except Exception as e:
        print("Error accessing:", url)
        print(e)
        return None


def write_html_to_file(html, filename):
    of = open(filename, "w")
    of.write(html.encode("utf-8"))
    # of.flush()
    of.close()


def get_browser_with_url(url, timeout=120, driver="firefox"):
    """Returns an open browser with a given url."""

    # choose a browser
    if driver == "firefox":
        browser = webdriver.Firefox()
    elif driver == "ie":
        browser = webdriver.Ie()
    elif driver == "chrome":
        browser = webdriver.Chrome()
    else:
        print("Driver choosen is not recognized")

    # set maximum load time
    browser.set_page_load_timeout(timeout)

    # open a browser with given url
    browser.get(url)

    time.sleep(0.5)

    return browser


def get_html_from_dynamic_site(url, timeout=120,
                               driver="firefox", attempts=10):
    """Returns html from a dynamic site, opening it in a browser."""

    RV = ""

    # try several attempts
    for i in range(attempts):
        try:
            # load browser
            browser = get_browser_with_url(url, timeout, driver)

            # get html
            time.sleep(2)
            content = browser.page_source

            # try again if there is no content
            if not content:
                browser.quit()
                raise Exception("No content!")

            # if there is content gets out
            browser.quit()
            RV = content
            break

        except:
            print("\nTry ", i, " of ", attempts, "\n")
            time.sleep(5)

    return RV


def timeit(func=None, loops=1, verbose=False):
    if func:
        def inner(*args, **kwargs):

            sums = 0.0
            mins = 1.7976931348623157e+308
            maxs = 0.0
            print('====%s Timing====' % func.__name__)
            for i in range(0, loops):
                t0 = time.time()
                result = func(*args, **kwargs)
                dt = time.time() - t0
                mins = dt if dt < mins else mins
                maxs = dt if dt > maxs else maxs
                sums += dt
                if verbose:
                    print('\t%r ran in %2.9f sec on run %s' %
                          (func.__name__, dt, i))
            print('%r min run time was %2.9f sec' % (func.__name__, mins))
            print('%r max run time was %2.9f sec' % (func.__name__, maxs))
            print('%r avg run time was %2.9f sec in %s runs' %
                  (func.__name__, old_div(sums, loops), loops))
            print('==== end ====')
            return result

        return inner
    else:
        def partial_inner(func):
            return timeit(func, loops, verbose)

        return partial_inner


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te - ts))
        return result

    return wrap
