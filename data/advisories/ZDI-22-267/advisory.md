# ZDI-22-267: Foxit PDF Reader OnMouseExit Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-267
- **ZDI-CAN:** ZDI-CAN-14848
- **Date:** 2022-02-10
- **CVE:** CVE-2022-24356
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** DoHyun Lee(@l33d0hyun)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-267/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the OnMouseExit method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2021-10-13 - Vulnerability reported to vendor
- 2022-02-10 - Coordinated public release of advisory
