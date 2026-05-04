# ZDI-13-007: Microsoft Internet Explorer Layout Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-007
- **ZDI-CAN:** ZDI-CAN-1550
- **Date:** 2013-02-01
- **CVE:** CVE-2012-2548
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 9
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles CCaret objects. After the CCaret object has been freed there exists a race condition to reclaim the target objects heap buffer before a background thread issues a message to update the screen caret and reuse the stale pointer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-063

## Disclosure Timeline

- 2012-11-09 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
