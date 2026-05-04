# ZDI-24-1155: PaperCut NG image-handler Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1155
- **ZDI-CAN:** ZDI-CAN-23859
- **Date:** 2024-08-22
- **CVE:** CVE-2024-4712
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** NG
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1155/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of PaperCut NG. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Web Print Image Handler. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-May-2024

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
