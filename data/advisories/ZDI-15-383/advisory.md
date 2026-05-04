# ZDI-15-383: Microsoft Internet Explorer Array Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-383
- **ZDI-CAN:** ZDI-CAN-2944
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2448
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-383/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Array's call function. The issue lies in the failure to properly ensure that the 'this' parameter is an object and not a native integer. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-079

## Disclosure Timeline

- 2015-05-21 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
