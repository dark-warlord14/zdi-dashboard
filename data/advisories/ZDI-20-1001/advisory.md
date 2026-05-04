# ZDI-20-1001: Microsoft Chakra Inline Cache Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1001
- **ZDI-CAN:** ZDI-CAN-10925
- **Date:** 2020-08-14
- **CVE:** CVE-2020-1555
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Asprose
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of inline caches. By performing actions in JavaScript, an attacker can trigger a read past the end of an allocated array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1555

## Disclosure Timeline

- 2020-06-02 - Vulnerability reported to vendor
- 2020-08-14 - Coordinated public release of advisory
