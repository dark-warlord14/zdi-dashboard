# ZDI-17-846: Microsoft Windows DNSAPI NSEC3_RecordRead Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-846
- **ZDI-CAN:** ZDI-CAN-5207
- **Date:** 2017-10-10
- **CVE:** CVE-2017-11779
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nelson William Gamazo Sanchez - Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-846/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DNS responses. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11779

## Disclosure Timeline

- 2017-09-22 - Vulnerability reported to vendor
- 2017-10-10 - Coordinated public release of advisory
