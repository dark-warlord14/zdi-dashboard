# ZDI-07-075: Microsoft Internet Explorer Element Tags Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-075
- **ZDI-CAN:** ZDI-CAN-230
- **Date:** 2007-12-11
- **CVE:** CVE-2007-5344
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of document objects that have been created, modified, deleted then accessed by JavaScript. By storing references to document nodes, then removing them by a separate reference, the document model in memory becomes unstable. Accessing the tags property while the document is in this unstable condition results in a heap corruption, allowing the execution of arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-069.mspx

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2007-12-11 - Coordinated public release of advisory
