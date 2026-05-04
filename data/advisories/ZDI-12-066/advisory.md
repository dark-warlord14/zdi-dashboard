# ZDI-12-066: Internet Explorer CTagFactory Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-066
- **ZDI-CAN:** ZDI-CAN-1479
- **Date:** 2012-04-18
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-066/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific issue is due to the process re-using a freed CTagFactory object. This can be made to occur by creating a specially crafted t:media element and later removing it. Remote attackers can abuse this to achieve arbitrary code execution under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-023

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-04-18 - Coordinated public release of advisory
