# ZDI-19-359: Microsoft Internet Explorer Property Put Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-359
- **ZDI-CAN:** ZDI-CAN-7757
- **Date:** 2019-04-15
- **CVE:** CVE-2019-0752
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-359/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of script commands that set certain properties of DOM objects. By performing actions in script, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0752

## Disclosure Timeline

- 2019-01-09 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
- 2019-11-01 - Advisory Updated
