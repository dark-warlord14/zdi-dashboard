# ZDI-20-691: ManageEngine OpManager OpmSkipFilter Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-691
- **ZDI-CAN:** ZDI-CAN-11127
- **Date:** 2020-06-09
- **CVE:** CVE-2020-13818
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpManager
- **Credit:** Yazhi Wang of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-691/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ManageEngine OpManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the OpmSkipFilter class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files in the context of the service account.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/network-monitoring/help/read-me-complete.html#125144

## Disclosure Timeline

- 2020-05-25 - Vulnerability reported to vendor
- 2020-06-09 - Coordinated public release of advisory
