# ZDI-22-968: BMC Track-It! HTTP Module Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-968
- **ZDI-CAN:** ZDI-CAN-16709
- **Date:** 2022-07-12
- **CVE:** CVE-2022-35865
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** BMC
- **Affected Products:** Track-It!
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-968/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of BMC Track-It!. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authorization of HTTP requests. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

BMC has issued an update to correct this vulnerability. More details can be found at: https://community.bmc.com/s/article/Security-vulnerabilities-patched-in-Track-It-Version-2

## Disclosure Timeline

- 2022-03-25 - Vulnerability reported to vendor
- 2022-07-12 - Coordinated public release of advisory
- 2022-07-14 - Advisory Updated
