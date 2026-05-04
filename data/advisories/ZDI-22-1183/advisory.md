# ZDI-22-1183: ManageEngine NetFlow Analyzer getDNSResolveOption Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1183
- **ZDI-CAN:** ZDI-CAN-17697
- **Date:** 2022-09-01
- **CVE:** CVE-2022-37024
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** NetFlow Analyzer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1183/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ManageEngine NetFlow Analyzer. Authentication is required to exploit this vulnerability. The specific flaw exists within the getDNSResolveOption function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/itom/advisory/cve-2022-37024.html

## Disclosure Timeline

- 2022-07-28 - Vulnerability reported to vendor
- 2022-09-01 - Coordinated public release of advisory
