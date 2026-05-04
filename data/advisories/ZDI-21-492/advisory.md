# ZDI-21-492: Synology DiskStation Manager Netatalk dsi_doff Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-492
- **ZDI-CAN:** ZDI-CAN-12326
- **Date:** 2021-04-29
- **CVE:** CVE-2021-31439
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Angelboy(@scwuaptx) from DEVCORE Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-492/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology DiskStation DS418play. Authentication is not required to exploit this vulnerablity. The specific flaw exists within the processing of DSI structures in Netatalk. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/zh-hk/security/advisory/Synology_SA_20_26

## Disclosure Timeline

- 2020-11-07 - Vulnerability reported to vendor
- 2021-04-29 - Coordinated public release of advisory
- 2021-05-24 - Advisory Updated
