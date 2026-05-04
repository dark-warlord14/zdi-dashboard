# ZDI-20-275: Horde Groupware Webmail Edition add Page Unrestricted File Upload Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-275
- **ZDI-CAN:** ZDI-CAN-10125
- **Date:** 2020-03-10
- **CVE:** CVE-2020-8866
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Horde
- **Affected Products:** Groupware Webmail Edition
- **Credit:** Andrea Cardaci
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-275/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Horde Groupware Webmail Edition. Authentication is required to exploit this vulnerability. The specific flaw exists within add.php. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the www-data user.

## Additional Details

Horde has issued an update to correct this vulnerability. More details can be found at: https://lists.horde.org/archives/announce/2020/001288.html

## Disclosure Timeline

- 2020-02-26 - Vulnerability reported to vendor
- 2020-03-10 - Coordinated public release of advisory
