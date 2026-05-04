# ZDI-24-443: (0Day) D-Link Network Assistant Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-443
- **ZDI-CAN:** ZDI-CAN-21426
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5292
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** Network Assistant
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-443/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of D-Link Network Assistant. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DNACore service. The service loads a file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

08/28/23 – ZDI reported the vulnerability to the vendor 08/24/23 – The vendor communicated that the cases would be fixed in Q4, 2023 release 05/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: On May 16, 2024, the vendor informed ZDI about v 4.0.0.21 EOL/EOS announcement https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10388

## Disclosure Timeline

- 2023-08-02 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
