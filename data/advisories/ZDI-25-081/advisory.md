# ZDI-25-081: TeamViewer Improper Neutralization of Argument Delimiters Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-081
- **ZDI-CAN:** ZDI-CAN-25816
- **Date:** 2025-02-03
- **CVE:** CVE-2025-0065
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TeamViewer
- **Affected Products:** TeamViewer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-081/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of TeamViewer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TeamViewer service, which listens on TCP port 5939 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

TeamViewer has issued an update to correct this vulnerability. More details can be found at: https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2025-1001/

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-02-03 - Coordinated public release of advisory
- 2025-02-03 - Advisory Updated
