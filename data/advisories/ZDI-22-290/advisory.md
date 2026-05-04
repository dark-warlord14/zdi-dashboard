# ZDI-22-290: BMC Track-It! HTTP Module Improper Access Control Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-290
- **ZDI-CAN:** ZDI-CAN-14618
- **Date:** 2022-02-10
- **CVE:** CVE-2022-24047
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** BMC
- **Affected Products:** Track-It!
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-290/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of BMC Track-It!. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authorization of HTTP requests. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

BMC has issued an update to correct this vulnerability. More details can be found at: https://community.bmc.com/s/article/Security-vulnerabilities-patched-in-Track-It

## Disclosure Timeline

- 2021-08-25 - Vulnerability reported to vendor
- 2022-02-10 - Coordinated public release of advisory
- 2022-02-11 - Advisory Updated
