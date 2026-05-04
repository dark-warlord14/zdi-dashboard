# ZDI-13-102: (Pwn2Own) Microsoft Internet Explorer VML Parsing Remote Code Execution Vulnerabillity

## Metadata

- **ZDI ID:** ZDI-13-102
- **ZDI-CAN:** ZDI-CAN-1828
- **Date:** 2013-05-29
- **CVE:** CVE-2013-2551
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VML data. The issue lies in the handling of an array when defined as an attribute of a subelement of a shape. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-037

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
- 2020-04-14 - Advisory Updated
