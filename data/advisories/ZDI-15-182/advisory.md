# ZDI-15-182: Microsoft Word ptCount Element Uninitialized Memory Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-182
- **ZDI-CAN:** ZDI-CAN-2789
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1682
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of embedded charts. By providing a malformed .docx file with an invalid "ptCount" node, an attacker can force uninitialized memory to be read. This allows for the execution of arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-046

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
