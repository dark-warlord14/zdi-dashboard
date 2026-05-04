# ZDI-11-123: Microsoft PowerPoint TimeCommandBehaviorContainer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-123
- **ZDI-CAN:** ZDI-CAN-949
- **Date:** 2011-04-12
- **CVE:** CVE-2011-0655
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-123/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ppcore.dll module responsible for parsing PowerPoint (ppt) files. When parsing a malformed TimeCommandBehaviorContainer structure the process raises an exception that causes an object in memory to be freed prior to being fully parsed. Due to the lack of a check that this object has been freed, a later function references an invalid pointer element. This can be leveraged by a remote attacker to execute arbitrary code under the context of the user running PowerPoint.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-022.mspx

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory
