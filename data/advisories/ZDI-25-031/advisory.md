# ZDI-25-031: Ivanti Endpoint Manager MyResolveEventHandler Untrusted Search Path Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-031
- **ZDI-CAN:** ZDI-CAN-25209
- **Date:** 2025-01-19
- **CVE:** CVE-2024-13158
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the MyResolveEventHandler method. The issue results from loading a library from an untrusted location. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-January-2025-for-EPM-2024-and-EPM-2022-SU6

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
