# ZDI-22-872: DevExpress SafeBinaryFormatter Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-872
- **ZDI-CAN:** ZDI-CAN-16710
- **Date:** 2022-06-24
- **CVE:** CVE-2022-28684
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** DevExpress
- **Affected Products:** DevExpress
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-872/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of DevExpress. Authentication is required to exploit this vulnerability. The specific flaw exists within the SafeBinaryFormatter library. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

The following updates resolve this issue: v22.1.1, v21.2.7, v21.1.9, v20.2.11, v20.1.15, v19.2.14, v19.1.15. v18.2.17, v18.1.18

## Disclosure Timeline

- 2022-03-16 - Vulnerability reported to vendor
- 2022-06-24 - Coordinated public release of advisory
