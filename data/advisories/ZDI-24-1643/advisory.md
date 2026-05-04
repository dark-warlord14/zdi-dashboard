# ZDI-24-1643: (Pwn2Own) iXsystems TrueNAS CORE tarfile.extractall Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1643
- **ZDI-CAN:** ZDI-CAN-25626
- **Date:** 2024-12-19
- **CVE:** CVE-2024-11944
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** iXsystems
- **Affected Products:** TrueNAS CORE
- **Credit:** Daan Keuper, Thijs Alkemade and Khaled Nassar from Computest Sector 7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1643/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of iXsystems TrueNAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the tarfile.extractall method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

iXsystems has issued an update to correct this vulnerability. More details can be found at: https://www.truenas.com/docs/core/13.0/gettingstarted/corereleasenotes/#130-u63

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-30 - Advisory Updated
