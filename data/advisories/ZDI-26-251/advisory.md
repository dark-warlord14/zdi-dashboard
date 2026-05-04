# ZDI-26-251: Foxit PDF Reader Update Service Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-251
- **ZDI-CAN:** ZDI-CAN-28595
- **Date:** 2026-04-02
- **CVE:** CVE-2026-3775
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Erik Egsgard of Field Effect
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-251/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Foxit PDF Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Foxit Reader Update Service. The product loads a library from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2025-12-31 - Vulnerability reported to vendor
- 2026-04-02 - Coordinated public release of advisory
- 2026-04-02 - Advisory Updated
