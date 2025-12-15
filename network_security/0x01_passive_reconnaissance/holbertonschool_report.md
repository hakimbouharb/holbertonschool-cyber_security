# Passive Reconnaissance Report — holbertonschool.com

> **Methodology:** Passive reconnaissance using **Shodan** (no direct interaction with target systems).
> **Scope:** holbertonschool.com and its subdomains.
> **Date:** *Fill when completed*
> **Analyst:** *Your Name*

---

## 1. Objective

Gather publicly available information about **holbertonschool.com** using Shodan to:

* Identify **IP ranges** associated with the domain
* Identify **technologies and frameworks** used across subdomains

---

## 2. Tools & Sources

* **Shodan** (search, host details)
* Optional correlation: DNS passive sources (Shodan DNS), SSL certs (Shodan)

> Note: No active scanning was performed.

---

## 3. Methodology

### 3.1 Domain & Subdomain Discovery (Passive)

* Use Shodan DNS and certificate transparency to enumerate subdomains.

**Example queries (Shodan):**

```text
domain:holbertonschool.com
hostname:holbertonschool.com
ssl.cert.subject.CN:holbertonschool.com
ssl.cert.subject.alt_names:holbertonschool.com
```

### 3.2 IP Range Identification

* For each discovered host, extract IPs and aggregate into ranges (CIDR where applicable).

**Example queries:**

```text
hostname:*.holbertonschool.com
org:"<Cloud Provider / ASN>"
```

### 3.3 Technology & Framework Identification

* Review Shodan service banners, HTTP headers, and detected technologies.

**Example queries:**

```text
http.title:"Holberton"
http.component:nginx OR http.component:apache
product:cloudflare
```

---

## 4. Findings

### 4.1 Identified IP Ranges

> *Populate from Shodan host results. Group by ASN / provider.*

| Provider / ASN | IP / Range   | Notes                           |
| -------------- | ------------ | ------------------------------- |
| *Example ASN*  | *x.x.x.x/xx* | *Observed via Shodan host data* |
|                |              |                                 |

---

### 4.2 Subdomains Observed

> *List subdomains discovered passively.*

| Subdomain                                                   | IP        | Provider          | Notes |
| ----------------------------------------------------------- | --------- | ----------------- | ----- |
| *[www.holbertonschool.com](http://www.holbertonschool.com)* | *x.x.x.x* | *Cloud / Hosting* |       |
|                                                             |           |                   |       |

---

### 4.3 Technologies & Frameworks

> *Based on Shodan service detection (HTTP headers, banners).*

| Subdomain                                                   | Technology       | Version (if any) | Evidence             |
| ----------------------------------------------------------- | ---------------- | ---------------- | -------------------- |
| *[www.holbertonschool.com](http://www.holbertonschool.com)* | *Nginx / Apache* | *-*              | *Shodan HTTP banner* |
|                                                             |                  |                  |                      |

**Common categories to check:**

* Web servers (Nginx, Apache)
* CDNs / WAFs (Cloudflare, Akamai)
* Frameworks (React, Next.js — if inferred)
* TLS / SSL details

---

## 5. Analysis

* **Infrastructure hosting:** *Summarize whether cloud/CDN is used.*
* **Attack surface (high-level):** *Only observational, no exploitation.*
* **Security posture (passive):** *Presence of CDN/WAF, TLS usage.*

---

## 6. Limitations

* Shodan visibility depends on indexed services.
* Some subdomains or IPs may not be indexed.
* No active validation was performed.

---

## 7. Conclusion

This passive reconnaissance provides an overview of the publicly observable infrastructure and technologies associated with **holbertonschool.com** using Shodan. The findings are suitable for academic analysis and defensive understanding.

---

## 8. References

* Shodan Documentation
* Passive Reconnaissance Best Practices
