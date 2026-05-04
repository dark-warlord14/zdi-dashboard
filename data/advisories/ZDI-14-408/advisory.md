# ZDI-14-408: Microsoft Internet Explorer CTreePos Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-408
- **ZDI-CAN:** ZDI-CAN-2522
- **Date:** 2014-12-09
- **CVE:** CVE-2014-6329
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Garage4Hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-408/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles an out-of-memory condition. By executing a script that consumes large amounts of memory, an attacker can cause a CTreePos object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-080.aspx

## Disclosure Timeline

- 2014-09-04 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
