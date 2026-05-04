# ZDI-17-729: Microsoft Windows PDF Library JPEG2000 Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-729
- **ZDI-CAN:** ZDI-CAN-4885
- **Date:** 2017-09-15
- **CVE:** CVE-2017-8728
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows PDF Library
- **Credit:** Giwan Go of STEALIEN & HIT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-729/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows PDF Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 graphics inside PDF documents. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8728

## Disclosure Timeline

- 2017-06-14 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
