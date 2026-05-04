# ZDI-16-288: Adobe Acrobat Reader DC ANAuthenticateResource Javascript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-288
- **ZDI-CAN:** ZDI-CAN-3427
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1041
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Matthias Kaiser
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ANAuthenticateResource method. By creating a specially crafted PDF with specific Javascript instructions, it is possible to bypass the Javascript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2015-12-01 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
