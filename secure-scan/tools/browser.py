
"""Browser-based page collection for SecureScan AI.

This module assumes the caller has already validated the target URL
against the configured authorization scope.
"""

import json
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from config import ACTIVE_PROBES, SENSITIVE_PATHS


def make_driver():
    """Create a headless Chrome driver with the logs our scanner needs."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,900")
    options.add_argument("--disable-gpu")

    # Chrome DevTools performance logs expose response metadata.
    options.set_capability(
        "goog:loggingPrefs",
        {"performance": "ALL", "browser": "ALL"},
    )

    return webdriver.Chrome(options=options)


def parse_perf_logs(entries):
    """Extract document response details, requested URLs, and redirects."""
    main = None
    requests_seen = set()
    redirects = 0

    for entry in entries:
        try:
            message = json.loads(entry["message"])["message"]
        except (KeyError, TypeError, ValueError):
            # Ignore malformed or unexpected Chrome log entries.
            continue

        method = message.get("method")
        params = message.get("params", {})

        if method == "Network.requestWillBeSent":
            url = params.get("request", {}).get("url", "")

            if url.startswith(("http://", "https://")):
                requests_seen.add(url)

            if (
                params.get("redirectResponse")
                and params.get("type") == "Document"
            ):
                redirects += 1

        elif method == "Network.responseReceived":
            if main is None and params.get("type") == "Document":
                main = params.get("response", {})

    return main or {}, sorted(requests_seen), redirects


JS_EXTRACT = """
const forms = Array.from(document.forms).map(f => ({
  action: f.action,
  method: (f.method || 'get').toLowerCase(),
  id: f.id || '',
  inputs: Array.from(f.elements).map(e => ({
    name: e.name || '',
    type: e.type || ''
  }))
}));

return {
  title: document.title,
  forms: forms,
  loose_password_inputs:
    document.querySelectorAll('input[type=password]').length,
  metas: Array.from(document.querySelectorAll('meta')).map(m => ({
    name: m.name || '',
    content: (m.content || '').slice(0, 80)
  })),
  scripts: Array.from(document.scripts).map(s => ({
    src: s.src || '',
    integrity: s.integrity || ''
  })),
  jquery: (window.jQuery && window.jQuery.fn &&
    window.jQuery.fn.jquery) || null,
  globals: {
    next: !!window.__NEXT_DATA__,
    react: !!window.React ||
      !!document.querySelector('[data-reactroot]'),
    vue: !!window.Vue || !!window.__VUE__,
    angular: !!window.ng ||
      !!document.querySelector('[ng-version]')
  }
};
"""


JS_PROBE = """
const paths = arguments[0];
const done = arguments[arguments.length - 1];

Promise.all(paths.map(p =>
  fetch(p, {credentials: 'omit', redirect: 'manual'})
    .then(async r => ({
      path: p,
      status: r.status,
      type: r.headers.get('content-type') || '',
      snippet: (await r.text()).slice(0, 300)
    }))
    .catch(() => ({
      path: p,
      status: 0,
      type: '',
      snippet: ''
    }))
)).then(done);
"""


def collect_page(url):
    """Load a previously authorized URL and return the scanner's page data."""
    driver = None

    try:
        driver = make_driver()
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(20)

        start = time.time()
        driver.get(url)

        WebDriverWait(driver, 15).until(
            lambda browser:
                browser.execute_script(
                    "return document.readyState"
                ) == "complete"
        )

        # Give single-page applications time to finish rendering.
        time.sleep(1.5)
        load_time = round(time.time() - start, 2)

        main, requests_seen, redirects = parse_perf_logs(
            driver.get_log("performance")
        )

        console_issues = [
            entry["message"][:200]
            for entry in driver.get_log("browser")
            if entry.get("level") in ("SEVERE", "WARNING")
        ][:15]

        source = driver.page_source

        # Probes run only when explicitly enabled in configuration.
        probes = (
            driver.execute_async_script(
                JS_PROBE, sorted(SENSITIVE_PATHS)
            )
            if ACTIVE_PROBES
            else []
        )

        page = {
            "final_url": driver.current_url,
            "status": main.get("status"),
            "headers": {
                key.lower(): value
                for key, value in (main.get("headers") or {}).items()
            },
            "security_details": main.get("securityDetails") or {},
            "protocol": main.get("protocol"),
            "redirects": redirects,
            "load_time": load_time,
            "cookies": driver.get_cookies(),
            "dom": driver.execute_script(JS_EXTRACT),
            "requests_seen": requests_seen,
            "console_issues": console_issues,
            "html_size": len(source),
            "hints": {
                "next": "/_next/" in source,
                "wordpress": (
                    "wp-content" in source or "wp-includes" in source
                ),
                "php": ".php" in source,
            },
            "probes": probes,
        }

        return {"page": page, "error": ""}

    except WebDriverException as exc:
        message = str(exc).strip().splitlines()[0]
        return {"error": f"Could not load the page: {message}"}

    finally:
        # Always release the browser, even if navigation or collection fails.
        if driver is not None:
            try:
                driver.quit()
            except WebDriverException:
                pass
