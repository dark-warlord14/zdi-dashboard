# ZDI-25-419: TeamViewer Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-419
- **ZDI-CAN:** ZDI-CAN-26660
- **Date:** 2025-06-25
- **CVE:** CVE-2025-36537
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TeamViewer
- **Affected Products:** TeamViewer
- **Credit:** Giuliano Sanfins(0x_alibabas) from SiDi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-419/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of TeamViewer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TeamViewer service, which listens on TCP port 5939 by default. The issue results from incorrect permissions on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

TeamViewer has issued an update to correct this vulnerability. More details can be found at: https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2025-1002/

## Disclosure Timeline

- 2025-03-30 - Vulnerability reported to vendor
- 2025-06-25 - Coordinated public release of advisory
- 2025-06-25 - Advisory Updated
