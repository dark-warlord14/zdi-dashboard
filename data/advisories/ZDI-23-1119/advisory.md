# ZDI-23-1119: Ivanti Avalanche FileStoreConfig Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1119
- **ZDI-CAN:** ZDI-CAN-21002
- **Date:** 2023-08-15
- **CVE:** CVE-2023-32564
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileStoreConfig app. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2023-05-30 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
