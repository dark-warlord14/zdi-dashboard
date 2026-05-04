# ZDI-25-200: Exim Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-200
- **ZDI-CAN:** ZDI-CAN-26250
- **Date:** 2025-04-07
- **CVE:** CVE-2025-30232
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Exim
- **Affected Products:** Exim
- **Credit:** Oliver Ford
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-200/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Exim. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the dp command line parameter. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Exim has issued an update to correct this vulnerability. More details can be found at: https://www.exim.org/static/doc/security/CVE-2025-30232.txt

## Disclosure Timeline

- 2025-03-13 - Vulnerability reported to vendor
- 2025-04-07 - Coordinated public release of advisory
- 2025-04-07 - Advisory Updated
