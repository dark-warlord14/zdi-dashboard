# ZDI-12-036: Microsoft Internet Explorer VML CDispScroller Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-036
- **ZDI-CAN:** ZDI-CAN-1457
- **Date:** 2012-02-22
- **CVE:** CVE-2012-0155
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the handling of VML element positioning. When appending a VML element to a textArea element a reference to a cDispScroller object can be improperly freed. The object is can be reused, and due to this object being freed, a later allocation can be located in this memory region. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS12-010

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
