# ZDI-17-730: Microsoft Office Word WordPerfect Document Converter Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-730
- **ZDI-CAN:** ZDI-CAN-4893
- **Date:** 2017-09-12
- **CVE:** CVE-2017-8744
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Lucas Leong of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-730/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the converter for WordPerfect documents. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8744

## Disclosure Timeline

- 2017-06-14 - Vulnerability reported to vendor
- 2017-09-12 - Coordinated public release of advisory
