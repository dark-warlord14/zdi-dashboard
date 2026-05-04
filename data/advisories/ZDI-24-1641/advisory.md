# ZDI-24-1641: Intel Computing Improvement Program PyInstaller Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1641
- **ZDI-CAN:** ZDI-CAN-21847
- **Date:** 2024-12-03
- **CVE:** CVE-2023-49797
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Intel
- **Affected Products:** Computing Improvement Program
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1641/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Intel Computing Improvement Program. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within PyInstaller. The issue results from the use of a vulnerable version of PyInstaller. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Intel has issued an update to correct this vulnerability. More details can be found at: https://github.com/pyinstaller/pyinstaller/security/advisories/GHSA-9w2p-rh8c-v9g5

## Disclosure Timeline

- 2023-09-07 - Vulnerability reported to vendor
- 2024-12-03 - Coordinated public release of advisory
- 2024-12-03 - Advisory Updated
