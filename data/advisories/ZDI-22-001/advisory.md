# ZDI-22-001: BMC Track-It! GetData Missing Authorization Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-001
- **ZDI-CAN:** ZDI-CAN-14527
- **Date:** 2022-01-06
- **CVE:** CVE-2021-35001
- **CVSS:** 3.1
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** BMC
- **Affected Products:** Track-It!
- **Credit:** Brandin Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-001/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of BMC Track-It!. Authentication is required to exploit this vulnerability. The specific flaw exists within the GetData endpoint. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

BMC has issued an update to correct this vulnerability. More details can be found at: https://community.bmc.com/s/article/Security-vulnerabilities-patched-in-Track-It

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
