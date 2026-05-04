# ZDI-20-127: Microsoft Office Graph Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-127
- **ZDI-CAN:** ZDI-CAN-9427
- **Date:** 2020-01-15
- **CVE:** CVE-2020-0652
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** L4Nce
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Graph COM object. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0652

## Disclosure Timeline

- 2019-11-12 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
