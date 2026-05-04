# ZDI-21-1299: Ivanti Avalanche Filestore Management Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1299
- **ZDI-CAN:** ZDI-CAN-14187
- **Date:** 2021-11-18
- **CVE:** CVE-2021-42125
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1299/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileStoreConfig app. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in version 6.3.3.

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-18 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
