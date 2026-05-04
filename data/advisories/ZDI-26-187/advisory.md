# ZDI-26-187: (Pwn2Own) Synology DiskStation Manager Netatalk Library Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-187
- **ZDI-CAN:** ZDI-CAN-19674
- **Date:** 2026-03-16
- **CVE:** CVE-2022-45188
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Kyle Zeng, Wil Gibbs, Jayakrishna Menon, and SEFCOM
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-187/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Synology DiskStation Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the afp_getappl function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_22_23

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
