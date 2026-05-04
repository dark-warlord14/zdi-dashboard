# ZDI-21-1301: Ivanti Avalanche EnterpriseServer Service Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1301
- **ZDI-CAN:** ZDI-CAN-15251
- **Date:** 2021-11-18
- **CVE:** CVE-2021-42133
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1301/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the saveConfig method. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in version 6.3.3.

## Disclosure Timeline

- 2021-09-29 - Vulnerability reported to vendor
- 2021-11-18 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
