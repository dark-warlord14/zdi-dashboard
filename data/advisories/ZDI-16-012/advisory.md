# ZDI-16-012: Adobe Reader DC Global Javascript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-012
- **ZDI-CAN:** ZDI-CAN-3362
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0943
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-012/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Global object. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to bypass the JavaScript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-02.html

## Disclosure Timeline

- 2015-10-15 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory
