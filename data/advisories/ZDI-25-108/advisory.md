# ZDI-25-108: (Pwn2Own) HP LaserJet Pro MFP 3301fdw suidexec Command Injection Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-108
- **ZDI-CAN:** ZDI-CAN-26611
- **Date:** 2025-03-03
- **CVE:** CVE-2025-26507
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** LaserJet Pro MFP 3301fdw
- **Credit:** Felipe Jacob Custodio Romero, Neodyme AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-108/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of HP LaserJet Pro MFP 3301fdw printers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the suidexec executable. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_11953771-11953793-16/hpsbpi04007

## Disclosure Timeline

- 2025-02-24 - Vulnerability reported to vendor
- 2025-03-03 - Coordinated public release of advisory
- 2025-03-03 - Advisory Updated
