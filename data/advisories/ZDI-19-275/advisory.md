# ZDI-19-275: Microsoft Internet Explorer event Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-275
- **ZDI-CAN:** ZDI-CAN-7691
- **Date:** 2019-03-12
- **CVE:** CVE-2019-0665
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-275/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the event object. By performing actions in script, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0665

## Disclosure Timeline

- 2018-12-19 - Vulnerability reported to vendor
- 2019-03-12 - Coordinated public release of advisory
