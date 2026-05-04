# ZDI-23-456: Ivanti Avalanche FileStoreConfig Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-456
- **ZDI-CAN:** ZDI-CAN-17812
- **Date:** 2023-04-24
- **CVE:** CVE-2023-28128
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-456/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileStoreConfig app. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2022-07-07 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
