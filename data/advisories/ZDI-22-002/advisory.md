# ZDI-22-002: BMC Track-It! Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-002
- **ZDI-CAN:** ZDI-CAN-14122
- **Date:** 2022-01-06
- **CVE:** CVE-2021-35002
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** BMC
- **Affected Products:** Track-It!
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of BMC Track-It!. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of email attachments. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

BMC has issued an update to correct this vulnerability. More details can be found at: https://community.bmc.com/s/article/Security-vulnerabilities-patched-in-Track-It

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
