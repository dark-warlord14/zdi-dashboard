# ZDI-20-588: Schneider Electric EcoStruxure IT Gateway Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-588
- **ZDI-CAN:** ZDI-CAN-10377
- **Date:** 2020-05-06
- **CVE:** CVE-2020-10626
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure IT Gateway
- **Credit:** Ryan Wincey (@rwincey) of Securifera
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-588/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric EcoStruxure IT Gateway. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of files within the Temp directory. The issue results from an incorrect assignment of privilege to a critical resource. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/ICSA2012601

## Disclosure Timeline

- 2020-03-31 - Vulnerability reported to vendor
- 2020-05-06 - Coordinated public release of advisory
