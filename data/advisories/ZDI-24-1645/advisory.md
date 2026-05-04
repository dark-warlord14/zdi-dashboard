# ZDI-24-1645: Progress Software WhatsUp Gold WriteDataFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1645
- **ZDI-CAN:** ZDI-CAN-24975
- **Date:** 2024-12-06
- **CVE:** CVE-2024-46909
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Andy Niu of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1645/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software WhatsUp Gold. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the WriteDataFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-September-2024

## Disclosure Timeline

- 2024-08-06 - Vulnerability reported to vendor
- 2024-12-06 - Coordinated public release of advisory
- 2024-12-06 - Advisory Updated
