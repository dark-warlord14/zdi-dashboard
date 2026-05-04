# ZDI-21-1332: Commvault CommCell AppStudioUploadHandler Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1332
- **ZDI-CAN:** ZDI-CAN-13894
- **Date:** 2021-11-22
- **CVE:** CVE-2021-34997
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Commvault
- **Affected Products:** CommCell
- **Credit:** kpc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1332/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Commvault CommCell. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the AppStudioUploadHandler class. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Fixed in Version 11.25

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-22 - Coordinated public release of advisory
