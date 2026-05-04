# ZDI-21-1183: Foxit PDF Reader Annotation Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1183
- **ZDI-CAN:** ZDI-CAN-14729
- **Date:** 2021-10-15
- **CVE:** CVE-2021-34952
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** ZhangJiaxing(@r0fm1a) from Codesafe Team of Legendsec at Qi'anxin Group
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1183/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Annotation objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2021-08-05 - Vulnerability reported to vendor
- 2021-10-15 - Coordinated public release of advisory
