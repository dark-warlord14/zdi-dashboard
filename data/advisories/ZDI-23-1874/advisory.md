# ZDI-23-1874: Foxit PDF Reader Annotation Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1874
- **ZDI-CAN:** ZDI-CAN-22259
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51560
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1874/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Annotation objects. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2023-10-19 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
