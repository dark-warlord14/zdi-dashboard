# ZDI-25-1039: (Pwn2Own) Synology BeeStation Plus auth_info Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1039
- **ZDI-CAN:** ZDI-CAN-28275
- **Date:** 2025-12-03
- **CVE:** CVE-2025-12686
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation Plus
- **Credit:** @Tek_7987 and @_Anyfun (both working @Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Synology BeeStation Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of the auth_info parameter. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_25_12

## Disclosure Timeline

- 2025-11-20 - Vulnerability reported to vendor
- 2025-12-03 - Coordinated public release of advisory
- 2025-12-03 - Advisory Updated
