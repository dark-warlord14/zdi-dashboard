# ZDI-09-086: Microsoft Internet Explorer XHTML DOM Manipulation Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-086
- **ZDI-CAN:** ZDI-CAN-496
- **Date:** 2009-12-08
- **CVE:** CVE-2009-3671
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Sam Thomas of eshu.co.uk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-086/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required in that a user must visit a malicious web page. The specific flaw exists in the manipulation and parsing of certain HTML tags. The ordering of various objects in a malformed way results in memory corruption resulting in a call to a dangling pointer which can be further leveraged via a heap spray. Exploitation of this vulnerability will lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-072.mspx

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-12-08 - Coordinated public release of advisory
