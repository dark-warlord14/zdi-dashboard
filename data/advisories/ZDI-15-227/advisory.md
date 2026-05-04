# ZDI-15-227: Microsoft Windows Type 1 Font callother Opcode Heap Buffer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-227
- **ZDI-CAN:** ZDI-CAN-2795
- **Date:** 2015-05-15
- **CVE:** CVE-2015-0092
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** s3tm3m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-227/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of certain Type 1 fonts. By providing a crafted font, an attacker can cause a negative offset to be used when calculating a heap buffer address. This would allow an attacker to execute arbitrary code as SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-021.aspx

## Disclosure Timeline

- 2015-03-04 - Vulnerability reported to vendor
- 2015-05-15 - Coordinated public release of advisory
