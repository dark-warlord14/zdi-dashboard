# ZDI-17-333: Bitdefender Internet Security cevakrnl Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-333
- **ZDI-CAN:** ZDI-CAN-4574
- **Date:** 2017-05-11
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Valentin Shilnenkov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-333/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within cevakrnl.xmd. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Fixed in cevakrnl.xmd (7.70464).

## Disclosure Timeline

- 2017-03-24 - Vulnerability reported to vendor
- 2017-05-11 - Coordinated public release of advisory
