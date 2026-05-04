# ZDI-25-657: Samsung MagicINFO 9 Server MagicInfoWebAuthorClient Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-657
- **ZDI-CAN:** ZDI-CAN-26519
- **Date:** 2025-07-28
- **CVE:** CVE-2025-54440
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** MagicINFO 9 Server
- **Credit:** Nicola `fromVeeko` Davico of Shielder, Paolo `paupu` Cavaglia of Shielder and Abdel Adim `smaury` Oisfi of Shielder
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-657/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung MagicINFO 9 Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MagicInfoWebAuthorClient app. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungtv.com/securityUpdates

## Disclosure Timeline

- 2025-03-25 - Vulnerability reported to vendor
- 2025-07-28 - Coordinated public release of advisory
- 2025-07-28 - Advisory Updated
