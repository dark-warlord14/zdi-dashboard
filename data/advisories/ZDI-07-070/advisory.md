# ZDI-07-070: Skype URI Handler Remote Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-070
- **ZDI-CAN:** ZDI-CAN-236
- **Date:** 2007-12-06
- **CVE:** CVE-2007-5989
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Skype
- **Affected Products:** Skype
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the 'skype4com' URI handler created by Skype during installation. When processing short string values through this handler an exploitable memory corruption may occur which can result in arbitrary code execution under the context of the current user.

## Additional Details

Skype has corrected this issue as of 11/15/2007. All clients updated or installed as of that date are patched to this issue.

## Disclosure Timeline

- 2007-11-02 - Vulnerability reported to vendor
- 2007-12-06 - Coordinated public release of advisory
