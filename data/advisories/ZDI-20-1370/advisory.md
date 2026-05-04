# ZDI-20-1370: Microsoft Chakra Array Iterator Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1370
- **ZDI-CAN:** ZDI-CAN-11871
- **Date:** 2020-11-11
- **CVE:** CVE-2020-17048
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Bruno Keith (@bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1370/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of array iterator objects. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17048

## Disclosure Timeline

- 2020-09-08 - Vulnerability reported to vendor
- 2020-11-11 - Coordinated public release of advisory
