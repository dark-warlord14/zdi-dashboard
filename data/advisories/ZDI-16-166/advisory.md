# ZDI-16-166: Microsoft Internet Explorer DOMImplementation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-166
- **ZDI-CAN:** ZDI-CAN-3403
- **Date:** 2016-02-10
- **CVE:** CVE-2016-0063
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-166/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer implements the DOMImplementation object. By performing certain script actions an attacker can cause Internet Explorer to execute the incorrect function, resulting in memory corruption. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-009

## Disclosure Timeline

- 2015-11-05 - Vulnerability reported to vendor
- 2016-02-10 - Coordinated public release of advisory
