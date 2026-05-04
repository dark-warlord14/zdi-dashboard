# ZDI-22-341: DevExpress SafeBinaryFormatter Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-341
- **ZDI-CAN:** ZDI-CAN-14619
- **Date:** 2022-02-15
- **CVE:** CVE-2021-36483
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** DevExpress
- **Affected Products:** DevExpress
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-341/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of DevExpress XtraReports. Authentication is required to exploit this vulnerability. The specific flaw exists within the SafeBinaryFormatter library. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in version v21.2.2

## Disclosure Timeline

- 2021-08-25 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
- 2022-03-10 - Advisory Updated
