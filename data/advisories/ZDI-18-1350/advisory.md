# ZDI-18-1350: Microsoft Edge Chakra Engine Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1350
- **ZDI-CAN:** ZDI-CAN-7409
- **Date:** 2018-11-20
- **CVE:** CVE-2018-8588
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1350/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of floating-point arrays in JIT code. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8588

## Disclosure Timeline

- 2018-10-26 - Vulnerability reported to vendor
- 2018-11-20 - Coordinated public release of advisory
- 2019-02-04 - Advisory Updated
