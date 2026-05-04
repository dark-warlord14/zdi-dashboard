# ZDI-23-670: (Pwn2Own) Lexmark MC3224i lbtraceapp Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-670
- **ZDI-CAN:** ZDI-CAN-19858
- **Date:** 2023-05-17
- **CVE:** CVE-2023-26067
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-670/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Lexmark MC3224i printers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the lbtraceapp binary. The code loads a binary from an unsecured location. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2023-26067.pdf

## Disclosure Timeline

- 2023-01-25 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
