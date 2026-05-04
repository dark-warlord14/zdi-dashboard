# ZDI-22-1038: Lexmark MC3224i Firmware Downgrade Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1038
- **ZDI-CAN:** ZDI-CAN-15981
- **Date:** 2022-08-02
- **CVE:** CVE-2022-24935
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** Christopher Anastasio @mufinnnnnnn and Justin Taft @JustTaft
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1038/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware upgrade feature. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2022-24935.pdf

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-08-02 - Coordinated public release of advisory
