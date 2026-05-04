# ZDI-24-056: Ivanti Avalanche FileStoreConfig Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-056
- **ZDI-CAN:** ZDI-CAN-21952
- **Date:** 2024-01-11
- **CVE:** CVE-2023-46263
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous and Lucas Miller of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileStoreConfig app. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-2-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2023-09-07 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
