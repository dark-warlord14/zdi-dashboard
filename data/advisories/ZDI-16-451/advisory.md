# ZDI-16-451: Microsoft Office Word RTF JPEG Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-451
- **ZDI-CAN:** ZDI-CAN-3743
- **Date:** 2016-08-09
- **CVE:** CVE-2016-3318
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Arun Kumar Sharma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-451/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of a JPEG embedded within an RTF file. The issue lies in the failure to properly validate user-supplied data which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-099

## Disclosure Timeline

- 2016-06-06 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory
