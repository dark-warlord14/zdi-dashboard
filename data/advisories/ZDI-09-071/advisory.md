# ZDI-09-071: Microsoft Internet Explorer writing-mode Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-071
- **ZDI-CAN:** ZDI-CAN-494
- **Date:** 2009-10-13
- **CVE:** CVE-2009-2531
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Internet Explorer 6, Internet Explorer 7, Internet Explorer 8
- **Credit:** Sam Thomas of eshu.co.uk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required in that a user must visit a malicious web page. The specific flaw exists in the parsing of CSS style information. When a writing-mode style is used with a specific combination of HTML tags, memory corruption occurs. Exploitation of this vulnerability will lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-054.mspx

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-10-13 - Coordinated public release of advisory
