# ZDI-24-1644: (Pwn2Own) iXsystems TrueNAS CORE fetch_plugin_packagesites tar Cleartext Transmission of Sensitive Information Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1644
- **ZDI-CAN:** ZDI-CAN-25668
- **Date:** 2024-12-19
- **CVE:** CVE-2024-11946
- **CVSS:** 3.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** iXsystems
- **Affected Products:** TrueNAS CORE
- **Credit:** Daan Keuper, Thijs Alkemade and Khaled Nassar from Computest Sector 7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1644/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to tamper with firmware update files on affected installations of iXsystems TrueNAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of firmware updates. The issue results from the use of an insecure protocol to deliver updates. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

iXsystems has issued an update to correct this vulnerability. More details can be found at: https://www.truenas.com/docs/core/13.0/gettingstarted/corereleasenotes/#130-u63

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-30 - Advisory Updated
