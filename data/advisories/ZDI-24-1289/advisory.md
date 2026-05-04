# ZDI-24-1289: TeamViewer Missing Authentication Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1289
- **ZDI-CAN:** ZDI-CAN-24623
- **Date:** 2024-09-26
- **CVE:** CVE-2024-7479
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** TeamViewer
- **Affected Products:** TeamViewer
- **Credit:** Peter Gabaldon (https://pgj11.com/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1289/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of TeamViewer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TeamViewer service, which listens on TCP port 5939 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

TeamViewer has issued an update to correct this vulnerability. More details can be found at: https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2024-1006/

## Disclosure Timeline

- 2024-08-01 - Vulnerability reported to vendor
- 2024-09-26 - Coordinated public release of advisory
- 2024-09-26 - Advisory Updated
