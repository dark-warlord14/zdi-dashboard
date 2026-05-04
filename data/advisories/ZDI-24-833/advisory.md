# ZDI-24-833: (Pwn2Own) Synology BC500 synocam_param.cgi Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-833
- **ZDI-CAN:** ZDI-CAN-22418
- **Date:** 2024-07-11
- **CVE:** CVE-2024-39349
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** BC500
- **Credit:** Freddy Ma, Jimmy Chang, Jimmy Liu (DrmnSamoLiu), Kyo Chen, Nancy Chang, Sébastien Dusuel (DuSu)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-833/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology BC500 cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the synocam_param.cgi module. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-id/security/advisory/Synology_SA_23_15

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-07-11 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
