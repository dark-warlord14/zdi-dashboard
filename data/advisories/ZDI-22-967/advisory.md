# ZDI-22-967: BMC Track-It! GetPopupSubQueryDetails SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-967
- **ZDI-CAN:** ZDI-CAN-16690
- **Date:** 2022-07-12
- **CVE:** CVE-2022-35864
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** BMC
- **Affected Products:** Track-It!
- **Credit:** Y4er
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-967/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of BMC Track-It!. Authentication is required to exploit this vulnerability. The specific flaw exists within the GetPopupSubQueryDetails endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

BMC has issued an update to correct this vulnerability. More details can be found at: https://community.bmc.com/s/article/Security-vulnerabilities-patched-in-Track-It-Version-2

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2022-07-12 - Coordinated public release of advisory
- 2022-07-14 - Advisory Updated
