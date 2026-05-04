# ZDI-14-416: Adobe Flash Player Regular Expression Object Out-Of-Bound Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-416
- **ZDI-CAN:** ZDI-CAN-2588
- **Date:** 2014-12-09
- **CVE:** CVE-2014-9162
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Wen Guanxing from Venustech ADLAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-416/
## Vulnerability Details

This vulnerability allows remote attackers to disclose arbitrary memory on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Regular Expression Objects. By matching a specially crafted regular expression, it is possible for an attacker to force out-of-bounds reads. An attacker can leverage this vulnerability to disclose arbitrary memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb14-27.html

## Disclosure Timeline

- 2014-11-04 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
