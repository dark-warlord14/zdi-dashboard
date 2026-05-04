# ZDI-14-112: Microsoft Internet Explorer CSS Out-Of-Bounds Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-112
- **ZDI-CAN:** ZDI-CAN-2132
- **Date:** 2014-04-23
- **CVE:** CVE-2014-0278
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-112/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSS properties objects. The issue lies in the ability to index outside the bounds of an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-010.aspx

## Disclosure Timeline

- 2014-02-06 - Vulnerability reported to vendor
- 2014-04-23 - Coordinated public release of advisory
