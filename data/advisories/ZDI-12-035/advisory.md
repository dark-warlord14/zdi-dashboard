# ZDI-12-035: Microsoft Internet Explorer CDispNode t:MEDIA Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-035
- **ZDI-CAN:** ZDI-CAN-1299
- **Date:** 2012-02-22
- **CVE:** CVE-2012-0011
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 9
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required in that a target must visit a malicious page or open a malicious file. The flaw exists within MSHTML, specifically the handling of an HTML time t:MEDIA element. A t:MEDIA element can be manipulated such that when the page is refreshed a reference to a freed CDispNode object remains allowing the repurpose of this region. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS12-010

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
