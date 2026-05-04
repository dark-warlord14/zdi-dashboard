# ZDI-20-990: Adobe Acrobat Pro DC Web2PDF:AppLinks JavaScript Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-990
- **ZDI-CAN:** ZDI-CAN-11166
- **Date:** 2020-08-12
- **CVE:** CVE-2020-9712
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Abdul-Aziz Hariri of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-990/
## Vulnerability Details

This vulnerability allows remote attackers to bypass JavaScript API restrictions on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within a hidden menu item. By performing actions in JavaScript, an attacker can cause the parsing of arbitrary HTML documents. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-48.html

## Disclosure Timeline

- 2020-06-02 - Vulnerability reported to vendor
- 2020-08-12 - Coordinated public release of advisory
