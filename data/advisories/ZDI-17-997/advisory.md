# ZDI-17-997: Adobe Flash LocaleID determinePreferredLocales Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-997
- **ZDI-CAN:** ZDI-CAN-5075
- **Date:** 2017-12-20
- **CVE:** CVE-2017-3114
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-997/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of LocaleID's determinePreferredLocales method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/in/security/products/flash-player/apsb17-33.html

## Disclosure Timeline

- 2017-08-04 - Vulnerability reported to vendor
- 2017-12-20 - Coordinated public release of advisory
