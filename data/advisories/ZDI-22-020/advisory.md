# ZDI-22-020: WordPress Core WP_Query SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-020
- **ZDI-CAN:** ZDI-CAN-15541
- **Date:** 2022-01-10
- **CVE:** CVE-2022-21661
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** WordPress
- **Affected Products:** Core
- **Credit:** ngocnb and khuyenn from GiaoHangTietKiem JSC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-020/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of WordPress Core. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WP_Query class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

WordPress has issued an update to correct this vulnerability. More details can be found at: https://wordpress.org/news/2022/01/wordpress-5-8-3-security-release/

## Disclosure Timeline

- 2021-10-22 - Vulnerability reported to vendor
- 2022-01-10 - Coordinated public release of advisory
