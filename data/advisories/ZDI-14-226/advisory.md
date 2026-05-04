# ZDI-14-226: Microsoft Internet Explorer Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-226
- **ZDI-CAN:** ZDI-CAN-2370
- **Date:** 2014-07-09
- **CVE:** CVE-2014-1769
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AbdulAziz Hariri HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CMarkup objects. The issue lies in the failure to properly initialize a variable prior to using it, leading to memory corruption. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-jun.aspx

## Disclosure Timeline

- 2014-06-06 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
