# ZDI-23-756: (0Day) VIPRE Antivirus Plus SetPrivateConfig Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-756
- **ZDI-CAN:** ZDI-CAN-19394
- **Date:** 2023-05-31
- **CVE:** CVE-2023-32176
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VIPRE
- **Affected Products:** Antivirus Plus
- **Credit:** Yulin Sung - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-756/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VIPRE Antivirus Plus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SetPrivateConfig method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

VIPRE has issued an update to correct this vulnerability. More details can be found at: https://success.vipre.com/en_US/antivirus-plus-release-notes/home-plus-release-notes-20230530

## Disclosure Timeline

- 2022-11-24 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
- 2024-10-08 - Advisory Updated
