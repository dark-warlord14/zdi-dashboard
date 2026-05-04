# ZDI-22-330: (Pwn2Own) Lexmark MC3224i Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-330
- **ZDI-CAN:** ZDI-CAN-15894
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44735
- **CVSS:** 5.5
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** David BERARD (@_p0ly_), Vincent FARGUES (@Karion_), Thomas IMBERT (@masthoon), from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-330/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of packet captures. When parsing the filter property, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44735.pdf

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
