# ZDI-16-181: Microsoft Windows OleLoadPicture Heap Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-181
- **ZDI-CAN:** ZDI-CAN-3367
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0092
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the OleLoadPicture function. User-supplied data is used to calculate a buffer length for allocation and the function can then write beyond the buffer boundary. An attacker can leverage this functionality to execute arbitrary code in the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS16-030

## Disclosure Timeline

- 2015-11-24 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
