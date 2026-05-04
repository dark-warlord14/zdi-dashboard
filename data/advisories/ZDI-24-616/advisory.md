# ZDI-24-616: Logsign Unified SecOps Platform Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-616
- **ZDI-CAN:** ZDI-CAN-24164
- **Date:** 2024-06-12
- **CVE:** CVE-2024-5716
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:L
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-616/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Logsign Unified SecOps Platform. Authentication is not required to exploit this vulnerability. The specific flaw exists within the password reset mechanism. The issue results from the lack of restriction of excessive authentication attempts. An attacker can leverage this vulnerability to reset a user's password and bypass authentication on the system.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/19316621924754-03-06-2024-Version-6-4-8-Release-Notes

## Disclosure Timeline

- 2024-05-31 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
