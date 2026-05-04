# ZDI-25-844: Microsoft Windows Subsystem for Linux WslCoreVm::Initialize Incorrect Privilege Management Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-844
- **ZDI-CAN:** ZDI-CAN-27541
- **Date:** 2025-08-14
- **CVE:** CVE-2025-53788
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** William Gamazo Sanchez and Nitesh Surana of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-844/
## Vulnerability Details

This vulnerability allows local attackers to read arbitrary files on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within WslCoreVm::Initialize method. The issue results from incorrect management of privileges. An attacker can leverage this vulnerability to read files in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53788

## Disclosure Timeline

- 2025-07-09 - Vulnerability reported to vendor
- 2025-08-14 - Coordinated public release of advisory
- 2025-08-14 - Advisory Updated
