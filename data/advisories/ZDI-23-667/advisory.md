# ZDI-23-667: (Pwn2Own) Lexmark MC3224i lbtraceapp _WriteTarFile Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-667
- **ZDI-CAN:** ZDI-CAN-19766
- **Date:** 2023-05-17
- **CVE:** CVE-2023-26067
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** pixelindigo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-667/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Lexmark MC3224i printers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the _WriteTarFile method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2023-26067.pdf

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
