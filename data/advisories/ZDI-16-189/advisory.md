# ZDI-16-189: Adobe Reader DC Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-189
- **ZDI-CAN:** ZDI-CAN-3022
- **Date:** 2016-03-08
- **CVE:** CVE-2016-1007
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-189/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of annotation gestures. The issue lies in the failure to properly initialize the gestures property prior to using it, leading to memory corruption. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-09.html

## Disclosure Timeline

- 2015-06-30 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
