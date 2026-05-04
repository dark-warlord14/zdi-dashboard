# ZDI-19-179: Microsoft Chakra JavaScript Loop Type Confusion Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-179
- **ZDI-CAN:** ZDI-CAN-7153
- **Date:** 2019-02-12
- **CVE:** CVE-2019-0593
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Bruno Keith (@bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-179/
## Vulnerability Details

This vulnerability allows remote attackers to produce abnormal program execution on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JIT compilation of loops. By performing actions in JavaScript, an attacker can trigger a type confusion condition. It may be possible for an attacker to leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0593

## Disclosure Timeline

- 2018-08-20 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
